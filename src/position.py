from abc import ABC
import math

class Position(ABC):

  def __init__(self, *args) -> None:
    pass


class CartesianPosition(Position):
  """
  This class represents a position using the cartesian coordinate system
  """

  def __init__(self, *args) -> None:
    super().__init__(*args)
    self.x = args[0]
    self.y = args[1]


  def cart_to_sphere(self):
    """
    Converts cartesian coordinates to spherical coordinates
    :return float r: distance from the origin to the point
    :return float theta: angle from the origin to the point
    """

    r = math.sqrt(self.x ** 2 + self.y ** 2)
    theta = math.tan(self.y / self.x)
    return r, theta


class SphericalPosition(Position):
  """
  This class represents a position using the spherical coordinate system
  """


  def __init__(self, *args) -> None:
    super().__init__(*args)
    self.r = args[0]
    self.theta = args[1]


  def sphere_to_cart(self):
    """
    Converts spherical coordinates to cartesian coordinates
    :return float x: distance along the x-axis
    :return float y: distance along the y-axis
    """

    x = self.r * math.cos(self.theta)
    y = self.r * math.sin(self.theta)
    return x, y
