import unittest
import io
import random
from unittest.mock import patch
from common import utility as util, insz as i


class TestUtilityValidation(unittest.TestCase):

    def test_valid_date_input(self):
        date_input: str = '12/12/2012'
        result: bool = util.is_valid_date(date_input)

        self.assertTrue(result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_date_input(self, mock_stdout):
        date_input: str = '32/13/2012'
        util.is_valid_date(date_input)

        self.assertEqual(mock_stdout.getvalue(), 'Invalid date input, please select a valid date\n')

    def test_valid_gender(self):
        gender_input: str = random.choice(['m', 'w', 'u'])
        result: bool = util.is_valid_gender(gender_input)

        self.assertTrue(result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_gender(self, mock_stdout):
        gender_input: str = random.choice('x')
        util.is_valid_gender(gender_input)

        self.assertEqual(mock_stdout.getvalue(), 'Invalid gender input, please pick between m, w or u\n')

    def test_valid_amount(self):
        amount_input: str = '10'
        result: bool = util.is_valid_amount(amount_input)

        self.assertTrue(result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_amount(self, mock_stdout):
        amount_input: str = 'aze'
        util.is_valid_amount(amount_input)

        self.assertEqual(mock_stdout.getvalue(), 'Invalid amount input, please select a valid amount\n')

    def test_valid_yes_or_no(self):
        yes_or_no_input: str = random.choice(['y', 'n'])
        result: bool = util.is_valid_yes_or_no_input(yes_or_no_input)

        self.assertTrue(result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_yes_or_no(self, mock_stdout):
        yes_or_no_input: str = 'x'
        util.is_valid_yes_or_no_input(yes_or_no_input)

        self.assertEqual(mock_stdout.getvalue(), 'Invalid input, please pick between y or n\n')

    def test_valid_insz(self):
        insz_input = '66041040332'
        result: bool = util.is_valid_insz(insz_input)

        self.assertTrue(result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_insz(self, mock_stdout):
        insz_input = '12121212312'
        util.is_valid_insz(insz_input)

        self.assertEqual(mock_stdout.getvalue(), 'Invalid insz input, please pick a valid insz number\n')

    def test_is_2000_date_true(self):
        post_2000_date: str = '12/07/2050'
        post_2000_insz: list[str] = i.handle_insz_generation(post_2000_date, 1, 'u')

        result: bool = util.is_2000_date(post_2000_insz[0])
        self.assertTrue(result)

    def test_is_2000_date_false(self):
        pre_2000_date: str = '12/07/1950'
        pre_2000_insz: list[str] = i.handle_insz_generation(pre_2000_date, 1, 'u')

        result: bool = util.is_2000_date(pre_2000_insz[0])
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
