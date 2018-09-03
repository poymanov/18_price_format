import unittest
from format_price import format_price


class FormatPriceCase(unittest.TestCase):
    def test_simple_number(self):
        price_origin = '3245.000000'
        price_expected = '3 245'

        self.assertEqual(price_expected, format_price(price_origin))

    def test_thousands(self):
        price_origin = '245245.000000'
        price_expected = '245 245'

        self.assertEqual(price_expected, format_price(price_origin))

    def test_million(self):
        price_origin = '3245245.00000'
        price_expected = '3 245 245'

        self.assertEqual(price_expected, format_price(price_origin))

    def test_incorrect_value(self):
        incorrect_value = 'test'

        self.assertIsNone(format_price(incorrect_value))


if __name__ == '__main__':
    unittest.main(verbosity=2)
