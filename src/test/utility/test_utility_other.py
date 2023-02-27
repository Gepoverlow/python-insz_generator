import unittest
from src.common import utility as util


class TestUtilityOther(unittest.TestCase):

    def test_date_refactorer_bis_gender_true_dob_true(self):
        result: str = util.date_refactorer_bis('12/12/2007', True, True)
        self.assertEqual(result, '12/52/2007')

    def test_date_refactorer_bis_gender_true_dob_false(self):
        result: str = util.date_refactorer_bis('12/12/2007', True, False)
        self.assertGreaterEqual(int(result[0:1]), 0)
        self.assertLessEqual(int(result[0:1]), 3)
        self.assertEqual(result[2:10], '/40/2007')

    def test_date_refactorer_bis_gender_false_dob_true(self):
        result: str = util.date_refactorer_bis('12/12/2007', False, True)
        self.assertEqual(result, '12/32/2007')

    def test_date_refactorer_bis_gender_false_dob_false(self):
        result: str = util.date_refactorer_bis('12/12/2007', False, False)
        self.assertGreaterEqual(int(result[0:1]), 0)
        self.assertLessEqual(int(result[0:1]), 3)
        self.assertEqual(result[2:10], '/20/2007')

    def test_detect_insz_gender_male(self):
        result: str = util.detect_insz_gender('12121275526')
        self.assertEqual(result, 'Male')

    def test_detect_insz_gender_female(self):
        result: str = util.detect_insz_gender('12121292649')
        self.assertEqual(result, 'Female')


if __name__ == "__main__":
    unittest.main()


