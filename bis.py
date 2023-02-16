from utility import \
    daily_serial_number_generator, \
    check_number_generator, date_format_generator,\
    date_refactorer_bis,\
    handle_date_input,\
    handle_amount_input,\
    handle_bis_is_gender_known_input,\
    handle_bis_is_birthday_known_input

from faker import Faker

fake = Faker()


def handle_bis_generation(is_gender_known, is_birthday_known, date, amount):
    generate_random_dates = False

    if date is None:
        generate_random_dates = True

    for i in range(int(amount)):
        if generate_random_dates is True:
            split_random_date = str(fake.date()).split('-')
            date = '{}/{}/{}'.format(split_random_date[2], split_random_date[1], split_random_date[0])

        correct_date = date_refactorer_bis(date, is_gender_known, is_birthday_known)

        formatted_date = date_format_generator(correct_date)
        daily_serial = daily_serial_number_generator('U')
        check_number = check_number_generator(correct_date, daily_serial)

        print('BIS -> ' + formatted_date + '-' + daily_serial + '.' + check_number)


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




