"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module.
    add is a function in calc module
    """

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(2, 3)

        self.assertEqual(res, 5)

    def test_subtract_numbers(self):
        """Test subtract numbers"""
        res = calc.subtract(5, 1)

        self.assertEqual(res, 4)
