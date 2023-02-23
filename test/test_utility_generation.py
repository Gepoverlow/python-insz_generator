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

    def test_date_format_generator(self):
        result: str = util.date_format_generator('21/02/1989')
        self.assertEqual(result, '89.02.21')

    def test_check_number_generator_pre_2000(self):
        date: str = '21/02/1970'
        dailty_serial: str = '717'
        result: str = util.check_number_generator(date, dailty_serial)
        self.assertEqual(result, '40')

    def test_check_number_generator_post_2000(self):
        date: str = '21/02/2070'
        dailty_serial: str = '717'
        result: str = util.check_number_generator(date, dailty_serial)
        self.assertEqual(result, '69')

    def test_daily_serial_generator_woman(self):
        gender: str = 'w'
        result: str = util.daily_serial_number_generator(gender)
        self.assertTrue(result.isnumeric())
        self.assertEqual(len(result), 3)
        self.assertEqual(int(result) % 2, 0)

    def test_daily_serial_generator_man(self):
        gender: str = 'm'
        result: str = util.daily_serial_number_generator(gender)
        self.assertTrue(result.isnumeric())
        self.assertEqual(len(result), 3)
        self.assertEqual(int(result) % 2, 1)

    def test_daily_serial_generator_unisex(self):
        gender: str = 'u'
        result: str = util.daily_serial_number_generator(gender)
        self.assertTrue(result.isnumeric())
        self.assertEqual(len(result), 3)


if __name__ == "__main__":
    unittest.main()
