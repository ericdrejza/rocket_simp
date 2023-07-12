import numpy as np

class Atmosphere:
  """
  The atmosphere class will set parameters for the environment in which the rocket will operate.
  Additional parameters and increasing complexity can be implemented to better simulate real world conditions.
  Units will be metric for consistency.
  """

  # Example: constant, ideal atmosphere

  def __init__(self, altitude):
    """
    :param altitude: h
    """
    self.altitude = altitude  # m
    self.density = self.density(altitude)
    self.gravity = self.gravity(altitude)
    self.pressure = self.pressure(altitude)
    self.temperature = self.temperature(altitude)
    self.viscosity = self.viscosity(altitude)

  def density(self, altitude):
    """
    calculates density
    :param altitude:
    :return:
    """
    rho = 1.225  # kg/m^3
    return rho

  def gravity(self, altitude):
    """
    calculates gravity
    :param altitude:
    :return:
    """
    g = 9.81  # m/s^2
    return g

  def pressure(self, altitude):
    """
    calculates pressure
    :param altitude:
    :return:
    """
    P = 101325  # kg/m/s^2
    return P

  def temperature(self, altitude):
    """
    calculates temperature
    :param altitude:
    :return:
    """
    T = np.arange(15, 0, -15/100)  # C
    return T

  def viscosity(self, altitude):
    """
    calculates viscosity
    :param altitude:
    :return:
    """
    mu = 1.81 * 10**-5  # m^2/s
    return mu


def main():
  h = np.arange(0, 100000, 1000)  # m
  atmosphere_example = Atmosphere(h)
  print(__name__)

if __name__ == '__main__':
  main()
