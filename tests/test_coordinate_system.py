import unittest

from src.coordinate_system import CartesianCoordinateSystem
from src.coordinate_system import SphericalCoordinateSystem

from src.position import CartesianPosition, SphericalPosition


class TestCartesianCoordinateSystem(unittest.TestCase):
  
  def test_create_position_cartesian(self):
    position = CartesianCoordinateSystem.createPosition(0, 5)
    self.assertEquals(CartesianPosition(position).x, 0)
    self.assertEquals(CartesianPosition(position).y, 5)
  

class TestSphericalCoordinateSystem(unittest.TestCase):
  
  def test_create_position_spherical(self):
    position = SphericalCoordinateSystem.createPosition(5, 0)
    self.assertEquals(SphericalPosition(position).r, 5)
    self.assertEquals(SphericalPosition(position).r, 0)


if __name__ == '__main__':
  unittest.main()