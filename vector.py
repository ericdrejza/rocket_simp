import numpy as np
import math

class Vector:
  """
  The vector class will create a vector object from a calculated value. It will
  create magnitude, direction, and component attributes.
  """

  def __init__(self, magnitude: float, alpha: float) -> None:
    """
    :param float magnitude: magnitude of the vector
    :param float alpha: angle of the vector
    """
    self.magnitude = magnitude
    self.angle = alpha
    self.direction = np.sign(magnitude)
    self.x_component = magnitude * math.cos(alpha)
    self.y_component = magnitude * math.sin(alpha)


def main():
  pass

if __name__ == '__main__':
  main()