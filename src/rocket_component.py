from abc import ABC
import math

from atmosphere import Atmosphere
from position import CartesianPosition
from rocket_log import RocketLog
from vector import Vector2, Vector3
import scipy.integrate as integrate


class RocketComponent(ABC):
  
  def __init__(self, alpha: float, position: CartesianPosition, velocity: Vector2) -> None:
    super().__init__()

    # Position
    self.alpha = alpha  # radians
    self.position = position  # m
    self.velocity = velocity

    # Mass Properties (Falcon 9 ex.)
    self.mass_fuel = 375000  # kg
    self.fuel_flow_rate = 1450  # kg/s
    self.mass_structure = 25000  # kg
    self.length = 70  # m
    self.width = 5.2  # m

    # Engine Properties
    self.area_exhaust = math.pi * (self.width / 2) ** 2
    self.pressure_exhaust = 70927.5  # N/m^2
    self.velocity_exhaust = 3000  # m/s

    # Forces
    self.drag_force = self.calc_drag_force()  # N
    self.gravity_force = self.calc_gravity_force()  # N
    self.lift_force = self.calc_lift_force()  # N
    self.thrust_force = self.calc_thrust_force()  # N

    # Atmosphere Object
    self.atmosphere = Atmosphere(self.position_y)

    # Rocket Log
    self.log = RocketLog()

  
  def calc_mass(self, time_step) -> float:
    """
    calculate total mass of the system
    :param float time_step: time difference from one state to the next
    :return float mass: mass of the rocket at a point in time
    """

    mass = self.mass_structure + self.mass_fuel - (self.fuel_flow_rate * time_step)
    return mass


  # Calculate Forces
  def calc_drag_force(self) -> Vector2:
    """
    calculate the drag force acting on the rocket
    :return float: drag
    """

    drag_coefficient = 0.75  # approximation, replace later
    drag_area = math.pi * (self.width / 2)**2
    drag = drag_coefficient * self.atmosphere.density * drag_area * self.velocity ** 2 / 2
    return Vector2(r=drag, theta=self.alpha + math.pi)


  def calc_gravity_force(self) -> Vector2:
    """
    calculate the gravitational force acting on the rocket
    :return float: gravity
    """
    gravitational_constant = 6.674 * 10**-11  # m^3/kg*s
    mass_earth = 5.9722 * 10**24  # kg
    radius_earth = 6.371 * 10**6  # m
    gravity = gravitational_constant * mass_earth * self.calc_mass(1) / (radius_earth + self.y_position**2)
    return Vector2(r=gravity, theta=3 * math.pi / 2)


  def calc_lift_force(self) -> Vector2:
    """
    calculate the lift force acting on the rocket
    :return float: lift
    """

    lift_coefficient = 1.5 #approximation, replace later, assume vertical launch
    lift_area = self.length * self.width
    lift = lift_coefficient * self.atmosphere.density * lift_area * self.velocity ** 2 / 2
    return Vector2(r=lift, theta=math.pi/2 + self.alpha)


  def calc_thrust_force(self) -> Vector2:
    """
    calculate the thrust force acting on the rocket
    :return float: thrust
    """

    momentum_thrust = self.fuel_flow_rate * self.velocity_exhaust
    pressure_thrust = (self.atmosphere.pressure - self.pressure_exhaust) * self.area_exhaust
    thrust_force = momentum_thrust + pressure_thrust
    return Vector2(r=thrust_force, theta=self.alpha)


  def sum_forces(self) -> Vector2:
    """
    Returns the sum of force in both the x and y directions
    :return Vector object: the resultant force vector
    """

    sum_forces_x = self.thrust_force.x + self.lift_force.x + self.drag_force.x + self.gravity_force.x
    sum_forces_y = self.thrust_force.y + self.lift_force.y + self.drag_force.y + self.gravity_force.y

    return Vector2(x=sum_forces_x, y=sum_forces_y)


  def calc_new_acceleration(self, force: Vector2, time_step: float) -> Vector2:
    """
    From the sum of forces, solves for acceleration
    :param Vector force: resultant force acting on the rocket component
    :param float time_step: time difference from one state to the next
    :return Vector acceleration: new acceleration of the rocket after timestep
    """

    a_x = force.x / self.mass
    a_y = force.y / self.mass

    return Vector2(x=a_x, y=a_y)


  def calc_new_velocity(self, acceleration: Vector2, time_step: float) -> Vector2:
    """
    From the acceleration, solves for velocity
    :param Vector acceleration: acceleration of the rocket component at this stage
    :param float time_step: time difference from one state to the next
    :return Vector velocity: new velocity of the rocket after timestep
    """

    v_x = self.velocity.x + acceleration.x * time_step
    v_y = self.velocity.y + acceleration.y * time_step

    return Vector2(x=v_x, y=v_y)


  def calc_new_position(self, velocity: Vector2, time_step: float) -> Vector2:
    """
    From the velocity, solves for position
    :param Vector velocity: velocity of the rocket component at this stage
    :param float time_step: time difference from one state to the next
    :return float position: new position of the rocket after timestep
    """

    p_x = self.position.x + velocity.x * time_step
    p_y = self.position.y + velocity.y * time_step

    return Vector2(x=p_x, y=p_y)


# Concrete Components
class HeadRocketComponent(RocketComponent):

  def __init__(self, altitude=0) -> None:
    super().__init__(altitude)


# Abstract Decorator
class RocketComponentDecorator(RocketComponent):
  
  def __init__(self, rocket_component, altitude=0) -> None:
    super().__init__(altitude)
    self.rocket_component = rocket_component


  def set_rocket_component(self, rocket_component: 'RocketComponent') -> None:
    """
    Set the rocket component
    :param RocketComponent rocket_component: The rocket component to be coupled with self
    """
    self.rocket_component = rocket_component

  
  def decouple_rocket_component(self) -> RocketComponent:
    """
    Represent the decoupling of two rocket components
    :return RocketComponent: The RocketComponent that this object decorates
    """
    # Save off RocketComponent to return
    rocket_component = self.rocket_component

    # Remove decorator from self.rocket_component
    self.rocket_component = None

    return rocket_component


def main():
  pass

if __name__ == '__main__':
  main()