import unittest
from unittest.mock import patch
from src.common import utility as util


class TestUtilityHandling(unittest.TestCase):

    @patch('builtins.input', return_value='')
    def test_empty_date_input_handling(self, input):
        self.assertEqual(util.handle_date_input(), None)

    @patch('builtins.input', return_value='12/12/2007')
    def test_valid_date_input_handling(self, input):
        self.assertEqual(util.handle_date_input(), '12/12/2007')

    @patch('builtins.input', side_effect=['32/12/2007', 'aaaaa', '12a12a1212', '12/12/2007'])
    def test_invalid_date_input_handling(self, input):
        self.assertEqual(util.handle_date_input(), '12/12/2007')

    @patch('builtins.input', return_value='')
    def test_empty_amount_input_handling(self, input):
        self.assertEqual(util.handle_amount_input(), 1)

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

    @patch('builtins.input', return_value='')
    def test_empty_gender_input_handling(self, input):
        self.assertEqual(util.handle_insz_gender_input(), 'U')

    @patch('builtins.input', return_value='m')
    def test_valid_man_gender_input_handling(self, input):
        self.assertEqual(util.handle_insz_gender_input(), 'm')

    @patch('builtins.input', return_value='w')
    def test_valid_woman_gender_input_handling(self, input):
        self.assertEqual(util.handle_insz_gender_input(), 'w')

    @patch('builtins.input', return_value='u')
    def test_valid_unisex_gender_input_handling(self, input):
        self.assertEqual(util.handle_insz_gender_input(), 'u')

    @patch('builtins.input', side_effect=['x', '123', '12/12/2012', 'w'])
    def test_invalid_gender_input_handling(self, input):
        self.assertEqual(util.handle_insz_gender_input(), 'w')

    @patch('builtins.input', return_value='')
    def test_empty_gender_known_input_handling(self, input):
        self.assertEqual(util.handle_is_gender_known_input(), True)

    @patch('builtins.input', return_value='y')
    def test_valid_yes_gender_known_input_handling(self, input):
        self.assertEqual(util.handle_is_gender_known_input(), True)

    @patch('builtins.input', return_value='n')
    def test_valid_no_gender_known_input_handling(self, input):
        self.assertEqual(util.handle_is_gender_known_input(), False)

    @patch('builtins.input', side_effect=['x', '123', '12/12/2012', 'n'])
    def test_invalid_gender_known_input_handling(self, input):
        self.assertEqual(util.handle_is_gender_known_input(), False)

    @patch('builtins.input', return_value='')
    def test_empty_dob_known_input_handling(self, input):
        self.assertEqual(util.handle_is_dob_known_input(), True)

    @patch('builtins.input', return_value='y')
    def test_valid_yes_dob_known_input_handling(self, input):
        self.assertEqual(util.handle_is_dob_known_input(), True)

    @patch('builtins.input', return_value='n')
    def test_valid_no_dob_known_input_handling(self, input):
        self.assertEqual(util.handle_is_dob_known_input(), False)

    @patch('builtins.input', side_effect=['x', '123', '12/12/2012', 'n'])
    def test_invalid_dob_known_input_handling(self, input):
        self.assertEqual(util.handle_is_dob_known_input(), False)

    @patch('builtins.input', side_effect=['', '08051036849'])
    def test_empty_insz_input_handling(self, input):
        self.assertEqual(util.handle_insz_input(), '08051036849')

    @patch('builtins.input', return_value='90041223661')
    def test_valid_insz_input_handling(self, input):
        self.assertEqual(util.handle_insz_input(), '90041223661')

    @patch('builtins.input', side_effect=['12121212312', 'azazazazeaz', '12/12/2012', '11041217445'])
    def test_invalid_insz_input_handling(self, input):
        self.assertEqual(util.handle_insz_input(), '11041217445')


if __name__ == "__main__":
    unittest.main()
