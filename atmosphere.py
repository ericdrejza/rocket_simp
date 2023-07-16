class Atmosphere:
  """
  The atmosphere class will set parameters for the environment in which the
  rocket will operate. Additional parameters and increasing complexity can be
  implemented to better simulate real world conditions. Units will be metric
  for consistency.
  """

  # Current Example: constant, simplified atmosphere
  # Constant values pulled from sea level at 15C

  def __init__(self, altitude: float) -> None:
    """
    :param altitude: current section of the atmosphere to calculate data for
    """
    self.density = calc_density(altitude)  # kg/m^3
    self.gravity = calc_gravity(altitude)  # m/s^2
    self.pressure = calc_pressure(altitude)  # N/m^2
    self.temperature = calc_temperature(altitude)  # C
    self.viscosity = calc_viscosity(altitude)  # N*s/m^2


def calc_density(altitude: float) -> float:
  """
  calculates density
  :param altitude: height
  :return: density
  """
  density = 1.225  # kg/m^3
  return density


def calc_gravity(altitude: float) -> float:
  """
  calculates gravity
  :param altitude: height
  :return: gravity
  """
  gravity = 9.81  # m/s^2
  return gravity


def calc_pressure(altitude: float) -> float:
  """
  calculates pressure
  :param altitude: height
  :return: pressure
  """
  pressure = 101325.0  # kg/m/s^2
  return pressure


def calc_temperature(altitude: float) -> float:
  """
  calculates temperature
  :param altitude: height
  :return: temperature
  """
  temperature = 15.0  # C
  return temperature


def calc_viscosity(altitude: float) -> float:
  """
  calculates viscosity
  :param altitude: height
  :return: viscosity
  """
  viscosity = 1.81 * 10**-5  # m^2/s
  return viscosity


def main():
  pass

if __name__ == '__main__':
  main()
