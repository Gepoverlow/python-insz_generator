import hug
from common.insz import handle_insz_generation


@hug.get()
def generate_insz(date: hug.types.text, amount: hug.types.number, gender: hug.types.text):
    insz_list: list[str] = handle_insz_generation(date, amount, gender)

    return {'insz': insz_list}
