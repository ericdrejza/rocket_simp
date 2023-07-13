class Atmosphere:
  """
  The atmosphere class will set parameters for the environment in which the rocket will operate.
  Additional parameters and increasing complexity can be implemented to better simulate real world conditions.
  Units will be metric for consistency.
  """

  # Current Example: constant, simplified atmosphere
  # Density and viscosity values pulled from sea level at 15C

  def __init__(self, altitude: float) -> None:
    """
    :param altitude: float
    """
    self.density = self.calc_density(altitude)
    self.gravity = self.calc_gravity(altitude)
    self.pressure = self.calc_pressure(altitude)
    self.temperature = self.calc_temperature(altitude)
    self.viscosity = self.calc_viscosity(altitude)


  def calc_density(self, altitude: float) -> float:
    """
    calculates density
    :param altitude: float
    :return: float
    """
    density = 1.225  # kg/m^3
    return density


  def calc_gravity(self, altitude: float) -> float:
    """
    calculates gravity
    :param altitude: float
    :return: float
    """
    gravity = 9.81  # m/s^2
    return gravity


  def calc_pressure(self, altitude: float) -> float:
    """
    calculates pressure
    :param altitude: float
    :return: float
    """
    pressure = 101325.0  # kg/m/s^2
    return pressure


  def calc_temperature(self, altitude: float) -> float:
    """
    calculates temperature
    :param altitude: float
    :return: float
    """
    temperature = 15.0  # C
    return temperature


  def calc_viscosity(self, altitude: float) -> float:
    """
    calculates viscosity
    :param altitude: float
    :return: float
    """
    viscosity = 1.81 * 10**-5  # m^2/s
    return viscosity


def main():
  pass

if __name__ == '__main__':
  main()
