import unittest
import sys
import random

# TODO improve this
sys.path.append('..')

from project import utility as util


class TestUtilityValidation(unittest.TestCase):

    def test_valid_date_input(self):
        date_input: str = '12/12/2012'
        result: bool = util.is_valid_date(date_input)

        self.assertTrue(result)

    def test_invalid_date_input(self):
        date_input: str = '32/13/2012'
        result: bool = util.is_valid_date(date_input)

        self.assertIsNot(result, True)

    def test_valid_gender(self):
        gender_input: str = random.choice(['m', 'w', 'u'])
        result: bool = util.is_valid_gender(gender_input)

        self.assertTrue(result)

    def test_invalid_gender(self):
        gender_input: str = random.choice('x')
        result: bool = util.is_valid_gender(gender_input)

        self.assertIsNot(result, True)

    def test_valid_amount(self):
        amount_input: str = '10'
        result: bool = util.is_valid_amount(amount_input)

        self.assertTrue(result)

    def test_invalid_amount(self):
        amount_input: str = 'aze'
        result: bool = util.is_valid_amount(amount_input)

        self.assertIsNot(result, True)

    def test_valid_yes_or_no(self):
        yes_or_no_input: str = random.choice(['y', 'n'])
        result: bool = util.is_valid_yes_or_no_input(yes_or_no_input)

        self.assertTrue(result)

    def test_invalid_yes_or_no(self):
        yes_or_no_input: str = 'x'
        result: bool = util.is_valid_yes_or_no_input(yes_or_no_input)

        self.assertIsNot(result, True)

    def test_valid_insz(self):
        insz_input = '66041040332'
        result: bool = util.is_valid_insz_input(insz_input)

        self.assertTrue(result)

    def test_invalid_insz(self):
        insz_input = '12121212312'
        result: bool = util.is_valid_insz_input(insz_input)

        self.assertIsNot(result, True)


if __name__ == "__main__":
    unittest.main()
