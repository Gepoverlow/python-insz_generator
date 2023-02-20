from utility import \
    daily_serial_number_generator, \
    check_number_generator, \
    date_format_generator, \
    handle_date_input, \
    handle_amount_input, \
    handle_insz_gender, \
    handle_insz_input, \
    is_2000_date, \
    detect_insz_gender

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


def handle_insz_decodification(insz_nr, is_post_2000_date, gender):
    birth_day = insz_nr[4:6]
    birth_month = insz_nr[2:4]
    birth_year = '20' + insz_nr[0:2] if is_post_2000_date else '19' + insz_nr[0:2]

    print('This persons birth day is {}/{}/{} and the gender is {}'.format(birth_day,
                                                                           birth_month,
                                                                           birth_year,
                                                                           gender))


def decode_insz():
    while True:
        try:
            insz = handle_insz_input()
            is_post_2000_date = is_2000_date(insz)
            gender = detect_insz_gender(insz)

            handle_insz_decodification(insz, is_post_2000_date, gender)
            break
        except:
            print('Something went wrong')
            break
