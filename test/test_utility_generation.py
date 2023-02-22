import unittest
import sys

# TODO improve this
sys.path.append('..')
from project import utility as util


class TestUtilityGeneration(unittest.TestCase):

    def test_odd_number_generator(self):
        result: str = util.odd_number_generator()
        self.assertNotEqual(int(result) % 2, 0)

    def test_even_number_generator(self):
        result: str = util.even_number_generator()
        self.assertEqual(int(result) % 2, 0)


if __name__ == "__main__":
    unittest.main()
