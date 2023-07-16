import numpy as np
import math

class Vector:
  """
  The vector class will create a vector object from a calculated value. It will
  create magnitude, direction, and component attributes.
  """

  def __init__(self, value: float, alpha: float) -> None:
    """
    :param value: float
    :param: alpha: float
    """
    self.magnitude = value
    self.angle = alpha
    self.direction = np.sign(value)
    self.x_component = value*math.cos(alpha)
    self.y_component = value*math.sin(alpha)


def main():
  pass

if __name__ == '__main__':
  main()