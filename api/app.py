import hug
from common.insz import insz_generator


@hug.get()
def generate_insz(date: hug.types.text = None, amount: hug.types.number = None, gender: hug.types.text = None):
    if date is None:
        date = '12/12/2017'

    if amount is None:
        amount = 1

    if gender is None:
        gender = 'u'

    insz_list: list[str] = insz_generator(date, amount, gender)

    return {'insz': insz_list}
