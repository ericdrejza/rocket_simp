from abc import ABC, abstractmethod
import math

class Position(ABC):

  def __init__(self, *args) -> None:
    pass
  
  
  @abstractmethod
  def get_altitude(self):
    pass



class CartesianPosition(Position):
  """
  This class represents a position using the cartesian coordinate system
  """
  
  def __init__(self, *args) -> None:
    super().__init__(*args)
    self.x = args[0]
    self.y = args[1]


  def __str__(self) -> str:
    return f'({self.x}, {self.y})'
  

  def get_altitude(self):
    return self.y


class SphericalPosition(Position):
  """
  This class represents a position using the spherical coordinate system
  """
  
  def __init__(self, *args) -> None:
    super().__init__(*args)
    self.r = args[0]
    self.theta = args[1]


  def __str__(self) -> str:
    return f'({self.r}, {self.theta})'
  

  def get_altitude(self):
    """
    Calculate the vertical distance

    :return float: The vertical distance of the position
    """
    return self.r * math.sin(self.theta)