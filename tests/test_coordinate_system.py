import unittest

from src.coordinate_system import CartesianCoordinateSystem
from src.coordinate_system import SphericalCoordinateSystem


class TestCartesianCoordinateSystem(unittest.TestCase):
  
  def test_create_position_cartesian(self):
    position = CartesianCoordinateSystem.createPosition(0, 5)
    self.assertEqual(position.x, 0)
    self.assertEqual(position.y, 5)
  

class TestSphericalCoordinateSystem(unittest.TestCase):
  
  def test_create_position_spherical(self):
    position = SphericalCoordinateSystem.createPosition(5, 0)
    self.assertEqual(position.r, 5)
    self.assertEqual(position.theta, 0)


if __name__ == '__main__':
  unittest.main()