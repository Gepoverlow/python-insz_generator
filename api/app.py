import hug
from faker import Faker
from api.validation import custom_types as t
from common.insz import insz_generator
from common import utility as u

fake = Faker()


@hug.get()
def generate_insz(date: t.date_type = None, amount: t.amount_type = None, gender: t.gender_type = None):
    if date is None:
        date: str = u.fake_date_generator()

    if amount is None:
        amount: int = 1

    if gender is None:
        gender: str = 'u'

    insz_list: list[str] = insz_generator(date, amount, gender)

    return {'insz': insz_list}
