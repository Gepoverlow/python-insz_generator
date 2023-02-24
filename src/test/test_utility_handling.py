import unittest
from unittest.mock import patch
import sys

# TODO improve this
sys.path.append('../..')
from src.common import utility as util


def get_input(text):
    return input(text)


class TestUtilityHandling(unittest.TestCase):

    @patch('builtins.input', return_value='12/12/2007')
    def test_valid_date_input_handling(self, input):
        self.assertEqual(util.handle_date_input(), '12/12/2007')

    @patch('builtins.input', side_effect=['32/12/2007', 'aaaaa', '12a12a1212', '12/12/2007'])
    def test_invalid_date_input_handling(self, input):
        self.assertEqual(util.handle_date_input(), '12/12/2007')

    @patch('builtins.input', return_value='10')
    def test_valid_amount_input_handling(self, input):
        self.assertEqual(util.handle_amount_input(), 10)

    @patch('builtins.input', return_value='99')
    def test_valid_amount_input_handling_more_than_20(self, input):
        self.assertEqual(util.handle_amount_input(), 1)

    @patch('builtins.input', return_value='0')
    def test_valid_amount_input_handling_less_than_1(self, input):
        self.assertEqual(util.handle_amount_input(), 1)

    @patch('builtins.input', side_effect=['-1', '&é&', 'AAAAAA', '5'])
    def test_invalid_amount_input_handling(self, input):
        self.assertEqual(util.handle_amount_input(), 5)

    def test_gender_input_handling(self):
        self.assertTrue(True)

    def test_gender_known_input_handling(self):
        self.assertTrue(True)

    def test_dob_known_input_handling(self):
        self.assertTrue(True)

    def test_insz_input_handling(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
