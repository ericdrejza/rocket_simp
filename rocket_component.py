from atmosphere import Atmosphere
import math


class Rocket:
  """
  The rocket class will calculate the forces acting upon the rocket component
  at a given time. Units will be metric for consistency.
  """

  def __init__(self) -> None:

    # Basic Properties (Falcon 9 ex.)
    self.altitude = 0  # m
    self.length = 70  # m
    self.width = 4  # m
    self.velocity = 1000  # m/s

    # Mass Properties (Falcon 9 ex.)
    self.mass_fuel = 375000  # kg
    self.mass_flow_rate = 1450  # kg/s
    self.mass_structure = 25000  # kg

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
    self.atmosphere = Atmosphere(self.altitude)


  def calc_mass(self) -> float:
    """
    calculate total mass of the system
    :return: mass of the rocket at a point in time
    """
    time_step = 1
    mass = self.mass_structure + self.mass_fuel - (self.mass_flow_rate * time_step)
    return mass


  def calc_drag_force(self) -> float:
    """
    calculate the drag force acting on the rocket
    :return: drag
    """

    drag_coefficient = 0.75  # approximation, replace later
    drag_area = math.pi * (self.width / 2)**2
    drag_force = drag_coefficient * self.atmosphere.density * drag_area * self.velocity ** 2 / 2
    return drag_force


  def calc_gravity_force(self) -> float:
    """
    calculate the gravitational force acting on the rocket
    :return: float
    """
    gravitational_constant = 6.674 * 10**-11  # m^3/kg*s
    mass_earth = 5.9722 * 10**24  # kg
    radius_earth = 6.371 * 10**6  # m
    gravity_force = gravitational_constant * mass_earth * self.calc_mass() / (radius_earth + self.altitude**2)
    return gravity_force


  def calc_lift_force(self) -> float:
    """
    calculate the lift force acting on the rocket
    :return: lift
    """

    lift_coefficient = 1.5 #approximation, replace later, assume vertical launch
    lift_area = self.length * self.width
    lift_force = lift_coefficient * self.atmosphere.density * lift_area * self.velocity ** 2 / 2
    return lift_force


  def calc_thrust_force(self) -> float:
    """
    calculate the thrust force acting on the rocket
    :return: thrust
    """

    momentum_thrust = self.mass_flow_rate * self.velocity_exhaust
    pressure_thrust = (self.atmosphere.pressure - self.pressure_exhaust) * self.area_exhaust
    thrust_force = momentum_thrust + pressure_thrust

    return thrust_force


def main():
  pass

if __name__ == '__main__':
  main()