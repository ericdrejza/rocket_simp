import math


class Vector2:
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
  def __init__(self, *, x=None, y=None, z=None, r=None, theta=None):
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
        raise ValueError('Cannot define a Vector by Rectangualr and Polar ' + 
                         'coordinate systems.  Use x and y or r and theta')
      else:
        self.x = x
        self.y = y
        self.update_polar()
    elif r is not None and theta is not None:
      self.r = r
      self.theta = theta
      self.update_cartesian()
    else:
      raise ValueError('Define a Vector by either x and y or r and theta')


  def update_polar(self) -> None:
    """
    Creates or updates polar coordinate attributes using cartesian coordinate
    attributes
    """
    self.r = math.sqrt(self.y ** 2 + self.x ** 2)
    self.theta = math.atan2(self.y, self.x)


  def update_cartesian(self) -> None:
    """
    Creates or updates cartesian coordinate attributes using polar coordinate
    attributes
    """
    self.x = self.r * math.cos(self.theta)
    self.y = self.r * math.sin(self.theta)


  def dot(self, other: 'Vector2') -> float:
    """
    Scaler product or dot product of vectors.  Projection of vector a onto 
    vector b

    Equation:
      dot = |magnitude_a|*|magnitude_b|*cos(theta_ab)
      this is equivalent to:
      dot = sum(a_i*b_i, i->n) 

    Parameters:
      self : Vector2
        Vector a in the above equation
      other : Vector2
        Vector b in the above equation

    Returns:
      dot : float
        resultant scalar value of above equation
    """
    dot = (self.x * other.x) + (self.y*other.y)

    return dot


  def cross(self, other: 'Vector2') -> float:
    """
    Vector product or cross product of vectors.  A vector perpendicular to both
    vector a and vector b. This is anticommutative such that a x b = - b x a

    In two dimensions, this is the determinant of the 2x2 matrix, a scalar

    Equation:
      cross = a x b = [a  b
                       c  d] = a*d - b*c

    Parameters:
      self : Vector2
        Vector a in the above equation
      other : Vector2
        Vector b in the above equation

    Returns:
      cross : float
        resultant scalar value of above equation
    """
    cross = (self.x * other.y) - (self.y * other.x)

    return cross


  def __add__(self, other: object) -> 'Vector2':
    """
    Adds two vectors together by their respective components

    Parameters:
      other : object
        the object to be added to self. if other is not an instance of Vector2
        raise an error

    Returns:
      new Vector2
        resultant Vector2 after adding respective x and y components
    """
    if isinstance(other, Vector2):
      x_resultant = self.x + other.x
      y_resultant = self.y + other.y
      return Vector2(x=x_resultant, y=y_resultant)
    else:
      raise NotImplementedError('Addition with a Vector2 is only defined for ' 
                                + 'another Vector2, not for type ' 
                                + str(type(other).__name__), '.')


  def __sub__(self, other: object) -> 'Vector2':
    """
    Subtracts two vectors by their respective components

    Parameters:
      other : object
        the object to be subtracted from self. if other is not an instance of 
        Vector2 raise an error

    Returns:
      new Vector2
        resultant Vector2 after subtracting respective x and y components
    """
    if isinstance(other, Vector2):
      x_resultant = self.x - other.x
      y_resultant = self.y - other.y
      return Vector2(x=x_resultant, y=y_resultant)
    else:
      raise NotImplementedError('Subtraction from a Vector2 is only defined ' +
                                'for another Vector2, not for type '+ 
                                str(type(other).__name__), '.')


  def __mul__(self, other: object) -> 'Vector2':
    if isinstance(other, Vector2):
      raise TypeError('Multiplication for two 2D vectors is not defined. Use '+
                      'vector2_a.dot(vector2_b) or vector2_a.cross(vector2_b) '
                      + 'for dot or cross product respectively.')
    elif isinstance(other, float) or isinstance(other, int):
      x_resultant = self.x * other
      y_resultant = self.y * other
      return Vector2(x=x_resultant, y=y_resultant)
    else:
      raise TypeError('Multiplication with a Vector2 is only defined ' +
                      'for scalar values (int or float), not for type ' +
                      str(type(other).__name__) + '.')


  def __truediv__(self, other: object) -> 'Vector2':
    pass


  def __floordiv__(self, other: object) -> 'Vector2':
    pass


  def __mod__(self, other: object) -> 'Vector2':
    pass


  def __pow__(self, other: object) -> 'Vector2':
    pass


  def __lt__(self, other: object):
    pass


  def __gt__(self, other: object):
    pass


  def __le__(self, other: object):
    pass


  def __ge__(self, other: object):
    pass


  def __eq__(self, other: object):
    pass


  def __ne__(self, other: object):
    pass


class Vector3():
  pass