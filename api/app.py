import hug
from common.insz import insz_generator


@hug.get()
def generate_insz(date: hug.types.text, amount: hug.types.number, gender: hug.types.text):
    insz_list: list[str] = insz_generator(date, amount, gender)

    return {'insz': insz_list}
