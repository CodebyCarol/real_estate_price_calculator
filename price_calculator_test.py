import unittest
from price_calculator import PriceCalculator

class PriceCalculatorTest(unittest.TestCase):
    
    def test_calculate_is_working(self):
        self.assertEqual(27500000, PriceCalculator.calculate(1, 10))
        self.assertEqual(30000000, PriceCalculator.calculate(2, 10))

    def test_bad_district(self):
        self.assertRaises(ValueError, PriceCalculator.calculate, 0, 10)

    def test_zero_squaremeter(self):
        self.assertRaises(ValueError, PriceCalculator.calculate, 1, 0)


if __name__ == "__main__":
    unittest.main()        