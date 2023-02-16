import random

from utility import \
    daily_serial_number_generator, \
    check_number_generator, date_format_generator,\
    handle_date_input,\
    handle_amount_input

from faker import Faker

fake = Faker()


def is_valid_yes_or_no_input(gender_known):
    if gender_known.lower() == 'y' or gender_known.lower() == 'n':
        return True
    else:
        print('Wrong input: Please enter Y for Yes or N for No')
        return False


def handle_bis_is_gender_known_input():
    while True:

        print('Is the gender known?')
        gender_known_input = input('> ')

        if gender_known_input == '':
            return True
        else:
            if is_valid_yes_or_no_input(gender_known_input):
                return True if gender_known_input == 'y' else False


def handle_bis_is_birthday_known_input():
    while True:

        print('Is the birthday known?')
        birthday_known_input = input('> ')

        if birthday_known_input == '':
            return True
        else:
            if is_valid_yes_or_no_input(birthday_known_input):
                return True if birthday_known_input == 'y' else False


def date_refactorer_bis(date, is_gender_known, is_birthday_known):
    split_date = date.split("/")

    if is_gender_known is True and is_birthday_known is True:
        return '{}/{}/{}'.format(split_date[0], str(int(split_date[1]) + 40), split_date[2])
    elif is_gender_known is False and is_birthday_known is True:
        return '{}/{}/{}'.format(split_date[0], str(int(split_date[1]) + 20), split_date[2])
    elif is_gender_known is True and is_birthday_known is False:
        return '{}/{}/{}'.format('0' + str(random.randint(0, 3)), '40', split_date[2])
    else:
        return '{}/{}/{}'.format('0' + str(random.randint(0, 3)), '20', split_date[2])


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




