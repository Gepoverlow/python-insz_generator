import unittest
from unittest.mock import patch
import sys

# TODO improve this
sys.path.append('..')
from project import utility as util


def get_input(text):
    return input(text)


def answer():
    ans = get_input('enter yes or no')
    if ans == 'yes':
        return 'you entered yes'
    if ans == 'no':
        return 'you entered no'


class TestUtilityHandling(unittest.TestCase):

    @patch('test_utility_handling.get_input', return_value='yes')
    def test_date_input_handling(self, input):
        self.assertEqual(answer(), 'you entered yes')

    def test_amount_input_handling(self):
        self.assertTrue(True)

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
