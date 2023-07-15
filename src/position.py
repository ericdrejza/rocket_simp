from abc import ABC

class Position(ABC):

  def __init__(self, *args) -> None:
    pass



class CartesianPosition(Position):
  """
  This class represents a position using the cartesian coordinate system
  """
  
  def __init__(self, *args) -> None:
    """
    Initializer for CartesianPosition
    """
    super().__init__(*args)
    self.x = args[0]
    self.y = args[1]


  def __str__(self) -> str:
    return f'({self.x}, {self.y})'
  


class SphericalPosition(Position):
  """
  This class represents a position using the spherical coordinate system
  """
  
  def __init__(self, *args) -> None:
    """
    Initializer for SphericalPosition
    """
    super().__init__(*args)
    self.r = args[0]
    self.theta = args[1]


  def __str__(self) -> str:
    return f'({self.r}, {self.theta})'