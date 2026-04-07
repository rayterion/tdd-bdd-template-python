from unittest import TestCase
from core.main import triangleArea

class TestMain(TestCase):
    def test_triangle_area(self):
        """ Test the triangleArea function with various inputs. """
        self.assertEqual(triangleArea(4, 5), 10)
        self.assertEqual(triangleArea(0, 5), 0)
        self.assertEqual(triangleArea(4, 0), 0)
        self.assertEqual(triangleArea(0, 0), 0)
    def test_triangle_area_negative(self):
        """ Test that triangleArea raises ValueError for negative inputs. """
        with self.assertRaises(ValueError):
            triangleArea(-1, 5)
        with self.assertRaises(ValueError):
            triangleArea(4, -1)
        with self.assertRaises(ValueError):
            triangleArea(-1, -1)