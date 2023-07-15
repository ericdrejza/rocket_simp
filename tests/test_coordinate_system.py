import unittest

from src.coordinate_system import CoordinateSystemCartesian
from src.coordinate_system import CoordinateSystemSpherical

from src.position import PositionCartesian, PositionSpherical


class TestCoordinateSystemCartesian(unittest.TestCase):
  
  def test_create_position_cartesian(self):
    position = CoordinateSystemCartesian.createPosition(0, 0)
    self.assertIsInstance(position, PositionCartesian,
      "Did not create an instance of PositionCartesian")
  

class TestCoordinateSystemSpherical(unittest.TestCase):
  
  def test_create_position_spherical(self):
    position = CoordinateSystemSpherical.createPosition(0, 0)
    self.assertIsInstance(position, PositionSpherical,
      "Did not create an instance of PositionSpherical")


if __name__ == '__main__':
  unittest.main()