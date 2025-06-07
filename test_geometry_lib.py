import math
import unittest
from geometry_lib import Circle, Triangle, area


class TestGeometryLib(unittest.TestCase):
    def test_circle(self):
        self.assertAlmostEqual(area(Circle(1)), math.pi)

    def test_triangle(self):
        self.assertAlmostEqual(area(Triangle(3, 4, 5)), 6)

    def test_is_right(self):
        self.assertTrue(Triangle(3, 4, 5).is_right())