import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(6, 3), 3)
        self.assertEqual(self.calc.subtract(-5, 7), -12)
        # Add more assertions to thoroughly test the add method.

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(6, 0), 0)
        self.assertEqual(self.calc.multiply(2, -4), -8)
        # Add more assertions to thoroughly test the add method.

    def test_divide_by_zero(self):
        """Test division by zero."""
        self.assertEqual(self.calc.divide(10, 0), None)

    def test_divide_valid(self):
        """Test valid division."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(9, 3), 3.0)

if __name__ == "__main__":
  unittest.main()