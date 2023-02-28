import unittest
from common import bis as b
from common import utility as u


class TestBisGeneration(unittest.TestCase):

    def test_bis_generation_gender_true_dob_true_amount_one(self):
        date: str = '12/12/2017'
        result: list[str] = b.bis_generator(True, True, date, 1)
        self.assertEqual(len(result), 1)

    def test_bis_generation_gender_true_dob_false_amount_one(self):
        date: str = '12/12/2017'
        result: list[str] = b.bis_generator(True, False, date, 1)
        self.assertEqual(len(result), 1)

    def test_bis_generation_gender_false_dob_true_amount_one(self):
        date: str = '12/12/2017'
        result: list[str] = b.bis_generator(False, True, date, 1)
        self.assertEqual(len(result), 1)

    def test_bis_generation_gender_false_dob_false_amount_one(self):
        date: str = '12/12/2017'
        result: list[str] = b.bis_generator(False, False, date, 1)
        self.assertEqual(len(result), 1)

    def test_bis_generation_gender_true_dob_true_amount_multiple(self):
        date: str = '12/12/2017'
        result: list[str] = b.bis_generator(True, True, date, 10)
        self.assertEqual(len(result), 10)

    def test_bis_generation_gender_true_dob_false_amount_multiple(self):
        date: str = '12/12/2017'
        result: list[str] = b.bis_generator(True, False, date, 10)
        self.assertEqual(len(result), 10)

    def test_bis_generation_gender_false_dob_true_amount_multiple(self):
        date: str = '12/12/2017'
        result: list[str] = b.bis_generator(False, True, date, 10)
        self.assertEqual(len(result), 10)

    def test_bis_generation_gender_false_dob_false_amount_multiple(self):
        date: str = '12/12/2017'
        result: list[str] = b.bis_generator(False, False, date, 10)
        self.assertEqual(len(result), 10)


if __name__ == "__main__":
    unittest.main()