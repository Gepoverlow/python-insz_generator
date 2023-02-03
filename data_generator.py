from util import handle_insz_date_input, handle_insz_amount_input


def generate_insz():
    while True:
        try:
            date = handle_insz_date_input()
            amount = handle_insz_amount_input()
            print(date)
            print(amount)
            break
        except:
            print('Something went wrong')
            break


def generate_bis():
    print('generated_bis')
