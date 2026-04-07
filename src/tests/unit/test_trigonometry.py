from core.trigonometry import Trigonometry
from unittest import TestCase

class TestTrigonometry(TestCase):
    def test_calculate_hypothenuse(self):
        """ Test the calculate_hypothenuse function with various inputs. """
        self.assertAlmostEqual(Trigonometry.calculate_hypothenuse(3, 4), 5)
        self.assertAlmostEqual(Trigonometry.calculate_hypothenuse(0, 4), 4)
        self.assertAlmostEqual(Trigonometry.calculate_hypothenuse(3, 0), 3)
        self.assertAlmostEqual(Trigonometry.calculate_hypothenuse(0, 0), 0)