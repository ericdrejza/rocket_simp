import math

class Vector:
  """
  The vector class will create a vector object from a calculated value. It will
  create magnitude, direction, and component attributes.

  Attributes:
    x : float
      value of x in cartesian coordinate system
    y : float
      value of x in cartesian coordinate system
    r: float
      value of radius in polar coordinate system
    theta : float
      value of theta (in radians) in polar coordinate system
  """

  def __init__(self, *, x=None, y=None, r=None, theta=None):
    """
    Initializes a vector from either cartesian or polar coordinate 
    representation.
    NOTE: Keyword arguments REQUIRED. Either define a vector with x and y 
    keywords for cartesian components, or r and theta for polar coordinates. 
    Initializer will throw a ValueError if both coordinate systems are used.
    
    Parameters:
      x : float
      value of x in cartesian coordinate system
      y : float
        value of x in cartesian coordinate system
      r: float
        value of radius in polar coordinate system
      theta : float
        value of theta (in radians) in polar coordinate system
    """

    if x is not None or y is not None:
      if r is not None or theta is not None:
        raise ValueError('Cannot define a Vector by Rectangualr and Polar \
                         coordinate systems.  Use x and y or r and theta')
      else:
        self.x = x
        self.y = y
        self.update_polar(x=self.x, y=self.y)
    elif r is not None and theta is not None:
      self.r = r
      self.theta = theta
      self.update_cartesian(self.r, self.theta)
    else:
      raise ValueError('Define a Vector by either x and y or r and theta')


  def update_polar(self) -> None:
    """
    Creates or updates polar coordinate attributes using cartesian coordinate
    attributes
    """

    self.r = math.tan(self.y/self.x)
    self.theta = math.atan2(self.y/self.x)


  def update_cartesian(self) -> None:
    """
    Creates or updates cartesian coordinate attributes using polar coordinate
    attributes
    """

    self.x = self.r * math.cos(self.theta)
    self.y = self.r * math.sin(self.theta)
