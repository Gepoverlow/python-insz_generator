import unittest
from common import insz as i
from common import utility as u


class TestInszGeneration(unittest.TestCase):

    def test_insz_generation_amount_one_gender_unisex(self):
        result: list[str] = i.insz_generator('12/12/2012', 1, 'u')
        self.assertEqual(len(result), 1)

        for j in result:
            self.assertTrue(u.is_insz_valid(j))

    def test_insz_generation_amount_multiple_gender_unisex(self):
        result: list[str] = i.insz_generator('12/12/2012', 5, 'u')
        self.assertEqual(len(result), 5)

        for j in result:
            self.assertTrue(u.is_insz_valid(j))

    def test_insz_generation_amount_one_gender_man(self):
        result: list[str] = i.insz_generator('12/12/2012', 1, 'm')
        self.assertEqual(len(result), 1)

        for j in result:
            self.assertTrue(u.is_insz_valid(j))

    def test_insz_generation_amount_multiple_gender_man(self):
        result: list[str] = i.insz_generator('12/12/2012', 5, 'm')
        self.assertEqual(len(result), 5)

        for j in result:
            self.assertTrue(u.is_insz_valid(j))

    def test_insz_generation_amount_one_gender_woman(self):
        result: list[str] = i.insz_generator('12/12/2012', 1, 'w')
        self.assertEqual(len(result), 1)

        for j in result:
            self.assertTrue(u.is_insz_valid(j))

    def test_insz_generation_amount_multiple_gender_woman(self):
        result: list[str] = i.insz_generator('12/12/2012', 5, 'w')
        self.assertEqual(len(result), 5)

        for j in result:
            self.assertTrue(u.is_insz_valid(j))

    def test_insz_decodification_pre_2000_date_man(self):
        insz_nr: str = '70121234771'
        detected_gender: str = u.insz_gender_detector(insz_nr)
        result: str = i.insz_decoder(insz_nr, False, detected_gender)
        self.assertEqual(result, 'This persons birth day is 12/12/1970 and the gender is Male')

    def test_insz_decodification_post_2000_date_man(self):
        insz_nr: str = '12121217128'
        detected_gender: str = u.insz_gender_detector(insz_nr)
        result: str = i.insz_decoder(insz_nr, True, detected_gender)
        self.assertEqual(result, 'This persons birth day is 12/12/2012 and the gender is Male')

    def test_insz_decodification_pre_2000_date_woman(self):
        insz_nr: str = '70121227843'
        detected_gender: str = u.insz_gender_detector(insz_nr)
        result: str = i.insz_decoder(insz_nr, False, detected_gender)
        self.assertEqual(result, 'This persons birth day is 12/12/1970 and the gender is Female')

    def test_insz_decodification_post_2000_date_woman(self):
        insz_nr: str = '12121230885'
        detected_gender: str = u.insz_gender_detector(insz_nr)
        result: str = i.insz_decoder(insz_nr, True, detected_gender)
        self.assertEqual(result, 'This persons birth day is 12/12/2012 and the gender is Female')


if __name__ == "__main__":
    unittest.main()

