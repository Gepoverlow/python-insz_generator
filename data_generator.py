from util import handle_insz_date_input, handle_insz_amount_input, handle_insz_gender, handle_insz_generation


def generate_insz():
    while True:
        try:
            date = handle_insz_date_input()
            amount = handle_insz_amount_input()
            gender = handle_insz_gender()

            handle_insz_generation(date, amount, gender)
            break
        except:
            print('Something went wrong')
            break


def generate_bis():
    print('generated_bis')
