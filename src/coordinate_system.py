from abc import ABC, abstractmethod
import numpy as np
from astropy.coordinates import cartesian_to_spherical
from astropy.coordinates import spherical_to_cartesian
from astropy.units import Quantity

from src.position import Position, CartesianPosition, SphericalPosition
# from vector import Vector


class CoordinateSystem(ABC):
  def __init__(self) -> None:
    pass

  @abstractmethod
  def createPosition() -> Position:
    pass


  # def createVector() -> Vector:
  #   pass



class CartesianCoordinateSystem(CoordinateSystem):
  def __init__(self) -> None:
    super().__init__()


  def createPosition(x, y) -> CartesianPosition:
    return CartesianPosition(x, y)
  

  def createPositionFromSpherical(spherical_position: SphericalPosition):
    x, y, z = spherical_to_cartesian(
      spherical_position.r, 0, spherical_position.theta)
    
    return CartesianCoordinateSystem.createPosition(x, y)



class SphericalCoordinateSystem(CoordinateSystem):
  def __init__(self) -> None:
    super().__init__()


  def createPosition(r, theta) -> SphericalPosition:
    return SphericalPosition(r, theta)


  def createPositionFromCartesian(cartesian_position: CartesianPosition):
    r, theta, psi = cartesian_to_spherical(
      cartesian_position.x, 0, cartesian_position.y)
    
    return SphericalCoordinateSystem.createPosition(r, theta)



### MAIN ###
def main():
  spherical_position = SphericalCoordinateSystem.createPosition(5, 0.2)
  cartesian_position = CartesianCoordinateSystem.createPositionFromSpherical(spherical_position)

  print(cartesian_position)


  spherical_position_2 = SphericalCoordinateSystem.createPositionFromCartesian(cartesian_position)

  print(spherical_position)
  print(spherical_position_2)
  print(type(spherical_position_2.theta))


if __name__ == '__main__':
  main()