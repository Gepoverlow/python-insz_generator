from general_util import handle_amount_input, handle_date_input, handle_insz_gender
from insz_util import handle_insz_generation
from bis_util import handle_bis_is_gender_known_input, handle_bis_is_birthday_known_input, handle_bis_generation


def generate_insz():
    while True:
        try:
            date = handle_date_input()
            amount = handle_amount_input()
            gender = handle_insz_gender()

            handle_insz_generation(date, amount, gender)
            break
        except:
            print('Something went wrong')
            break


def generate_bis():
    while True:
        try:
            is_gender_known = handle_bis_is_gender_known_input()
            is_birthday_known = handle_bis_is_birthday_known_input()
            date = handle_date_input()
            amount = handle_amount_input()

            handle_bis_generation(is_gender_known, is_birthday_known, date, amount)
            break
        except:
            print('Something went wrong')
            break
