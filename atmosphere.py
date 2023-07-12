class Atmosphere:
  """
  The atmosphere class will set parameters for the environment in which the rocket will operate.
  Additional parameters and increasing complexity can be implemented to better simulate real world conditions.
  Units will be metric for consistency.

  Current parameters include:
  altitude: h
  density: rho(h)
  gravity: g(h)
  pressure: P(h)
  temperature: T(h)
  viscosity: mu(h)
  """

  def __init__(self, altitude, density, gravity, pressure, temperature, viscosity):
    self.altitude = altitude  # m
    self.density = density  # kg/m^3
    self.gravity = gravity  # m/s^2
    self.pressure = pressure  # kg/m/s^2
    self.temperature = temperature  # C
    self.viscosity = viscosity  # m^2/s


# Example: constant, ideal atmosphere
import numpy as np

h = np.arange(0, 100000, 1000)  # m         sea level to the Karman Line (edge of space)
rho = 1.225                     # kg/m^3    average density of air at sea level
g = 9.81                        # m/s^2     standard value for gravity
P = 101325                      # kg/m/s^2  1 atm converted into
T = np.arange(15, 0, -15/100)   # C         temp at sea level to temp in a vacuum
mu = 1.81 * 10 ** -5            # m^2/s     average viscosity of air at sea level
atmosphere_example = Atmosphere(h, rho, g, P, T, mu)
