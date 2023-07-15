import unittest

from src.coordinate_system import CartesianCoordinateSystem
from src.coordinate_system import SphericalCoordinateSystem

from src.position import CartesianPosition, SphericalPosition


class TestCartesianCoordinateSystem(unittest.TestCase):
  
  def test_create_position_cartesian(self):
    position = CartesianCoordinateSystem.createPosition(0, 0)
    self.assertIsInstance(position, CartesianPosition,
      "Did not create an instance of CartesianPosition")
  

class TestSphericalCoordinateSystem(unittest.TestCase):
  
  def test_create_position_spherical(self):
    position = SphericalCoordinateSystem.createPosition(0, 0)
    self.assertIsInstance(position, SphericalPosition,
      "Did not create an instance of SphericalPosition")


if __name__ == '__main__':
  unittest.main()