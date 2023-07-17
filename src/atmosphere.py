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
    :param float altitude: current section of the atmosphere to calculate data for
    """
    self.update_atmosphere(altitude)


  def update_atmosphere(self, altitude: float) -> None:
    """
    :param altitude: float
    """
    self.density = self.calc_density(altitude)
    self.gravity = self.calc_gravity(altitude)
    self.pressure = self.calc_pressure(altitude)
    self.temperature = self.calc_temperature(altitude)
    self.viscosity = self.calc_viscosity(altitude)


def calc_density(altitude: float) -> float:
  """
  calculates density
  :param float altitude: altitude to calc density at
  :return float: density
  """
  density = 1.225  # kg/m^3
  return density


def calc_gravity(altitude: float) -> float:
  """
  calculates gravity
  :param float altitude: altitude to calc gravity at
  :return float: gravity
  """
  gravity = 9.81  # m/s^2
  return gravity


def calc_pressure(altitude: float) -> float:
  """
  calculates pressure
  :param float altitude: altitude to calc pressure at
  :return float: pressure
  """
  pressure = 101325.0  # kg/m/s^2
  return pressure


def calc_temperature(altitude: float) -> float:
  """
  calculates temperature
  :param float altitude: altitude to calc temperature at
  :return float: temperature
  """
  temperature = 15.0  # C
  return temperature


def calc_viscosity(altitude: float) -> float:
  """
  calculates viscosity
  :param float altitude: altitude to calc viscosity at
  :return float: viscosity
  """
  viscosity = 1.81 * 10**-5  # m^2/s
  return viscosity



### MAIN ###
def main():
  pass

if __name__ == '__main__':
  main()
