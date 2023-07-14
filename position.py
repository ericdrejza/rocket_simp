from abc import ABC

class Position(ABC):

  def __init__(self, *args) -> None:
    pass


class PositionCartesian(Position):
  """
  This class represents a position using the cartesian coordinate system
  """
  
  def __init__(self, *args) -> None:
    """
    Initializer for PositionCartesian
    """
    super().__init__(*args)
    self.x = args[0]
    self.y = args[1]


class PositionSpherical(Position):
  """
  This class represents a position using the spherical coordinate system
  """
  
  def __init__(self, *args) -> None:
    """
    Initializer for PositionSpherical
    """
    super().__init__(*args)
    self.r = args[0]
    self.theta = args[1]

