from abc import ABC, abstractmethod
from astropy.coordinates import cartesian_to_spherical
from astropy.coordinates import spherical_to_cartesian

from position import Position, CartesianPosition, SphericalPosition
# from vector import Vector


class CoordinateSystem(ABC):
  """
  Abstract Factory
  """

  def __init__(self) -> None:
    pass


  @abstractmethod
  def createPosition() -> Position:
    """
    Create and return a Position object

    :rtype: Position
    """
    pass



class CartesianCoordinateSystem(CoordinateSystem):
  """
  Coordinate System class that 
  """

  def __init__(self) -> None:
    super().__init__()


  def createPosition(x, y) -> CartesianPosition:
    """
    Creates a CartesianPosition from x and y coordinates

    :param float x: x coordinate in meters
    :param float y: y coordinate in meters

    :return CartesianPosition: CartesianPosition composed of the specified x and y
    """
    return CartesianPosition(x, y)
  

  def createPositionFromSpherical(spherical_position: SphericalPosition):
    """
    Create a CartesianPosition from a SphericalPosition

    :param SphericalPosition spherical_position: a SphericalPosition that you want to create a Position from

    :return CartesianPosition: The CartesianPosition representation of the given SphericalPosition
    """
    x, y, z = spherical_to_cartesian(
      spherical_position.r, 0, spherical_position.theta)
    
    return CartesianCoordinateSystem.createPosition(x, y)



class SphericalCoordinateSystem(CoordinateSystem):
  def __init__(self) -> None:
    super().__init__()


  def createPosition(r, theta) -> SphericalPosition:
    """
    Creates a SphericalPosition from r and theta parameters

    :param float r: The distance from the origin
    :param float theta: The angle with respect to the x-axis in radians

    :return CartesianPosition: CartesianPosition composed of the specified x and y
    """
    return SphericalPosition(r, theta)


  def createPositionFromCartesian(cartesian_position: CartesianPosition):
    """
    Create a SphericalPosition from a CartesianPosition

    :param CartesianPosition cartesian_position: a CartesianPosition that you want to create a SphericalPosition from

    :return CartesianPosition: The SphericalPosition representation of the given CartesianPosition
    """
    r, theta, psi = cartesian_to_spherical(
      cartesian_position.x, 0, cartesian_position.y)
    
    return SphericalCoordinateSystem.createPosition(r, theta)



### MAIN ###
def main():
  pass

if __name__ == '__main__':
  main()