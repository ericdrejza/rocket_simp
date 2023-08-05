from abc import ABC, abstractmethod
import math
import os

import scipy.integrate as integrate

from atmosphere import Atmosphere
from position import CartesianPosition
import rocket_log as rl
from vector import Vector


class RocketComponent(ABC):
  
  def __init__(self, id, alpha=(math.pi / 2),
    position:CartesianPosition=CartesianPosition(0, 0),
    velocity:Vector=Vector(x=0, y=0), keep_log=True) -> None:
    
    self.id = id

    # Spatial Properties
    self.alpha = alpha
    self.position = position  # m
    self.velocity = velocity

    # Atmosphere Object
    self.atmosphere = Atmosphere(self.position.y)

    # Mass Properties (Falcon 9 ex.)
    self.mass_fuel = 375000  # kg
    self.fuel_flow_rate = 1450 # kg/s
    self.mass_structure = 25000 # kg
    self.length = 70 # m
    self.width = 5.2 # m

    # Engine Properties
    self.area_exhaust = math.pi * (self.width / 2) ** 2
    self.pressure_exhaust = 70927.5  # N/m^2
    self.velocity_exhaust = 3000 * 9 # m/s

    # Forces
    self.drag_force = self.calc_drag_force()  # N
    self.gravity_force = self.calc_gravity_force()  # N
    self.lift_force = self.calc_lift_force()  # N
    self.thrust_force = self.calc_thrust_force()  # N

    # Rocket Log
    self.rocket_log = rl.RocketLog() if keep_log else None


  def calc_acceleration(self, force: Vector, time_step: float) -> Vector:
    """
    From the sum of forces, solves for acceleration

    Args:
      force Vector: resultant force acting on the rocket component
    :return Vector acceleration: acceleration of the rocket
    """
    mass_avg = self.get_total_mass() + \
      ((self.calc_new_fuel_mass(time_step) - self.mass_fuel) / 2)

    a_x = force.x / mass_avg
    a_y = force.y / mass_avg
    return Vector(x=a_x, y=a_y)


  # Calculate Forces
  def calc_drag_force(self) -> Vector:
    """
    calculate the drag force acting on the rocket
    :return Vector: drag
    """
    drag_coefficient = 0.75  # approximation, replace later
    drag_area = math.pi * (self.width / 2) ** 2
    drag = drag_coefficient * self.atmosphere.density * drag_area * \
      self.velocity.r ** 2 / 2
    return Vector(r=drag, theta=self.alpha + math.pi)


  def calc_gravity_force(self) -> Vector:
    """
    calculate the gravitational force acting on the rocket
    :return Vector: gravity
    """
    gravitational_constant = 6.674 * (10 ** -11)  # m^3/kg*s
    mass_earth = 5.9722 * (10 ** 24)  # kg
    radius_earth = 6.371 * (10 ** 6)  # m
    gravity = gravitational_constant * mass_earth * self.get_total_mass() \
      / ((radius_earth + self.position.y) ** 2)
    return Vector(r=gravity, theta=3 * math.pi / 2)


  def calc_lift_force(self) -> Vector:
    """
    calculate the lift force acting on the rocket
    :return Vector: lift
    """
    # lift_coefficient = 1.5 #approximation, replace later, assume vertical launch
    lift_coefficient = 0 # temp to handle vertical launch
    lift_area = self.length * self.width
    lift = lift_coefficient * self.atmosphere.density * lift_area * \
      self.velocity.r ** 2 / 2
    return Vector(r=lift, theta=math.pi/2 + self.alpha)
  

  def calc_new_fuel_mass(self, time_step) -> float:
    """
    Calculate the new fuel mass

    Returns:
      float: calculated fuel mass
    """
    new_fuel_mass = self.mass_fuel - (self.fuel_flow_rate * time_step)
    return max(0, new_fuel_mass)


  def calc_new_position(self, velocity: Vector, time_step: float) \
    -> CartesianPosition:
    """
    From the velocity, solves for position
    :param Vector velocity: velocity of the rocket component at this stage
    :param float time_step: time difference from one state to the next
    :return Position: new position of the rocket after time_step
    """
    p_x = self.position.x + velocity.x * time_step
    p_y = self.position.y + velocity.y * time_step
    return CartesianPosition(p_x, p_y)
  

  def calc_new_velocity(self, acceleration: Vector, time_step: float) \
    -> Vector:
    """
    From the acceleration, solves for velocity
    :param Vector acceleration: acceleration of the rocket component at this stage
    :param float time_step: time difference from one state to the next
    :return Vector: new velocity of the rocket after timestep
    """
    v_x = self.velocity.x + acceleration.x * time_step
    v_y = self.velocity.y + acceleration.y * time_step
    return Vector(x=v_x, y=v_y)


  def calc_percent_thrust_and_leftover_time(self, time_step):
    """
    Determine what portion of thrust we can use with remaining fuel and the
    time step.

    Args:
      time_step float: duration
    
    Returns:
      tuple():
        [0]: percentage of thrust to be used
        [1]: the remaining time to be used for sequential operations
    """
    percent_thrust = min(self.mass_fuel / (self.fuel_flow_rate * time_step), 1)
    leftover_time = 0
    if percent_thrust < 1:
      leftover_time = time_step - (percent_thrust * time_step)
    return (percent_thrust, leftover_time)


  def calc_thrust_force(self, percent_thrust:float=1) -> Vector:
    """
    Calculate the thrust force acting on the rocket

    Args:
      percent_thrust float: This float should be between 0 and 1

    Return:
      Vector: thrust force
    """
    if percent_thrust < 0 or percent_thrust > 1:
      raise ValueError
    
    momentum_thrust = percent_thrust * \
      (self.fuel_flow_rate * self.velocity_exhaust)
    pressure_thrust = (self.atmosphere.pressure - self.pressure_exhaust) * \
      self.area_exhaust
    thrust_force = momentum_thrust + pressure_thrust
    return Vector(r=thrust_force, theta=self.alpha)


  def get_total_mass(self):
    """
    Returns the total mass of this component and its children
    """
    mass = self.mass_fuel + self.mass_structure
    return mass


  def log(self, time: float):
    """
    Log our RocketComponent with RocketLog

    :param float time: The current time
    """
    if self.rocket_log is not None:
      return self.rocket_log.add(self, time)
    return None
  

  def output_log(self):
    self.rocket_log.data.to_json(
      os.path.join(os.path.dirname(__file__), f'rocket_component_{self.id}.log'),
      indent=4, orient='records')


  def string_info(self) -> None:
    """
    Print information about the rocket component
    """
    rocket_string = f'{self.id}, {self.position}, ' + \
      f'({round(self.velocity.x, 3)}, {round(self.velocity.y, 3)})'
    return rocket_string
  

  def sum_forces(self) -> Vector:
    """
    Returns the sum of force in both the x and y directions
    :return Vector object: the resultant force vector
    """
    sum_forces_x = self.thrust_force.x + self.lift_force.x + \
      self.drag_force.x + self.gravity_force.x
    sum_forces_y = self.thrust_force.y + self.lift_force.y + \
      self.drag_force.y + self.gravity_force.y

    return Vector(x=sum_forces_x, y=sum_forces_y)


  def update(self, time: float, time_step: float, lazy=False) -> None:
    """
    Update rocket component with the new time and time_step

    Parameters:
      time float: Current time
      time_step float: The duration captured by this update
    """
    percent_thrust, leftover_time = self.calc_percent_thrust_and_leftover_time(
      time_step)

    # Calculate new force vectors
    self.drag_force = self.calc_drag_force()
    self.gravity_force = self.calc_gravity_force()
    self.lift_force = self.calc_lift_force()
    self.thrust_force = self.calc_thrust_force(percent_thrust=percent_thrust)
    force = self.sum_forces()

    # Calculate new acceleration vector
    acceleration = self.calc_acceleration(force, time_step)

    # Set new values for velocity and position
    self.velocity = self.calc_new_velocity(acceleration, time_step)
    self.position = self.calc_new_position(self.velocity, time_step)

    # Set new value for remaining fuel mass
    self.mass_fuel = self.calc_new_fuel_mass(time_step)

    # Set new atmostphere values
    self.atmosphere.update(self.position.x)

    # Log
    self.log(time)
    return leftover_time



# Concrete Components
class HeadRocketComponent(RocketComponent):

  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)


  def update(self, time: float, time_step: float, lazy=False) -> None:
    """
    Process for updating a HeadRocketComponent

    *Refer to superclass update function*
    """
    super().update(time, time_step)


# Abstract Decorator
class RocketComponentDecorator(RocketComponent):
  
  def __init__(self, rocket_component, altitude=0) -> None:
    super().__init__(altitude)
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


  def get_total_mass(self):
    """
    *Refer to superclass get_total_mass method*
    """
    if self.rocket_component is None:
      return super().get_total_mass()
    else:
      return super().get_total_mass() + self.rocket_component.get_total_mass()


  def output_log(self):
    super().output_log()
    if self.rocket_component:
      self.rocket_component.output_log()


  def print(self):
    """
    Print RocketComponents
    """
    if self.rocket_component:
      self.rocket_component.print()
    super().print()


  def set_rocket_component(self, rocket_component: 'RocketComponent') -> None:
    """
    Set the rocket component
    :param RocketComponent rocket_component: The rocket component to be coupled
    with self
    """
    self.rocket_component = rocket_component
  

  def update(self, time: float, time_step: float, lazy=False) -> None:
    """
    *Refer to superclass update method*
    """
    """For a RocketComponentDecorator: if a two stage rocket is taking off, the 
    lowest stage on the vertical axis would be the decorator, and the head
    would be the highest.
    The decorator should first determine how the rocket is moving because it
    has thrusters"""
    if not lazy:
      left_over_time = super().update(time, time_step)
    if self.rocket_component is not None:
      # Have child copy self properties
      self.rocket_component.atmosphere = self.atmosphere
      self.rocket_component.position = self.position
      self.rocket_component.velocity = self.velocity
      self.rocket_component.drag_force = self.drag_force
      self.rocket_component.thrust_force = self.thrust_force
      self.rocket_component.gravity_force = self.gravity_force
      self.rocket_component.lift_force = self.lift_force

      self.rocket_component.update(time, left_over_time, lazy=lazy)



### MAIN ###
def main():
  head = HeadRocketComponent(0)
  head.print()
  head.update(1, 1)
  head.print()

if __name__ == '__main__':
  main()