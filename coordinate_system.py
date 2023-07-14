from abc import ABC, abstractmethod
import numpy as np
from astropy.coordinates import cartesian_to_spherical
from astropy.coordinates import spherical_to_cartesian
from astropy.units import Quantity

from position import Position, PositionCartesian, PositionSpherical
# from vector import Vector


class CoordinateSystem(ABC):
  def __init__(self) -> None:
    pass

  @abstractmethod
  def createPosition() -> Position:
    pass


  # def createVector() -> Vector:
  #   pass



class CoordinateSystemCartesian(CoordinateSystem):
  def __init__(self) -> None:
    super().__init__()


  def createPosition(x, y) -> PositionCartesian:
    return PositionCartesian(x, y)
  

  def createPositionFromSpherical(spherical_position: PositionSpherical):
    x, y, z = spherical_to_cartesian(
      spherical_position.r, 0, spherical_position.theta)
    
    return CoordinateSystemCartesian.createPosition(x, y)



class CoordinateSystemSpherical(CoordinateSystem):
  def __init__(self) -> None:
    super().__init__()


  def createPosition(r, theta) -> PositionSpherical:
    return PositionSpherical(r, theta)


  def createPositionFromCartesian(cartesian_position: PositionCartesian):
    r, theta, psi = cartesian_to_spherical(
      cartesian_position.x, 0, cartesian_position.y)
    
    return CoordinateSystemSpherical.createPosition(r, theta)


def main():
  spherical_position = CoordinateSystemSpherical.createPosition(5, 0.2)
  cartesian_position = CoordinateSystemCartesian.createPositionFromSpherical(spherical_position)

  print(cartesian_position)


  spherical_position_2 = CoordinateSystemSpherical.createPositionFromCartesian(cartesian_position)

  print(spherical_position)
  print(spherical_position_2)
  print(type(spherical_position_2.theta))


if __name__ == '__main__':
  main()