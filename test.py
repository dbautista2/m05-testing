import unittest
from fractions import Fraction

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()


# This test is saying that the expected result was 1, but the actual result was 9, 10
