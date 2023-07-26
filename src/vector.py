import math

class Vector:
  """
  The vector class will create a vector object from a calculated value. It will
  create magnitude, direction, and component attributes.
  """

  def __init__(self, x, y):
    """
    Initializes a vector from spherical components
    :param x: x-component
    :param y: y-component
    """

    self.x = x
    self.y = y
    self.r = math.tan(y/x)
    self.angle = math.atan(self.y/x)


  @classmethod
  def from_spherical(cls, magnitude: float, angle: float):
    """
    Initializes a vector from cartesian components
    :param float magnitude: magnitude of the vector
    :param float angle: angle of the vector
    """

    x_component = magnitude * math.cos(angle)
    y_component = magnitude * math.sin(angle)
    return Vector(x_component, y_component)
