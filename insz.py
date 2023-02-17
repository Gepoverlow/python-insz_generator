from utility import \
    daily_serial_number_generator,\
    check_number_generator,\
    date_format_generator,\
    handle_date_input, \
    handle_amount_input, \
    handle_insz_gender, \
    handle_insz_input, \
    handle_date_year

from faker import Faker

fake = Faker()


def handle_insz_generation(date, amount, gender):
    generate_random_dates = False

    if date is None:
        generate_random_dates = True

    for i in range(int(amount)):
        if generate_random_dates is True:
            split_random_date = str(fake.date()).split('-')
            date = '{}/{}/{}'.format(split_random_date[2], split_random_date[1], split_random_date[0])

        formatted_date = date_format_generator(date)
        daily_serial = daily_serial_number_generator(gender)
        check_number = check_number_generator(date, daily_serial)

        print('INSZ -> ' + formatted_date + '-' + daily_serial + '.' + check_number)


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


def decode_insz():
    while True:
        try:
            insz = handle_insz_input()
            is_post_2000_date = handle_date_year(insz)
            print(is_post_2000_date)
            break
        except:
            print('Something went wrong')
            break



