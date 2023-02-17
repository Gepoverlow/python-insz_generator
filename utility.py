import datetime
import random
from random import randint


def odd_number_generator(n_from, n_to):
    return random.choice([i for i in range(n_from, n_to + 1) if i % 2 != 0])


def even_number_generator(n_from, n_to):
    return random.choice([i for i in range(n_from, n_to) if i % 2 == 0])


def date_format_generator(date):
    split_date = date.split("/")
    return split_date[2][2:4] + '.' + split_date[1] + '.' + split_date[0]


def is_valid_gender(gender):
    if gender.lower() == 'm' or gender.lower() == 'w' or gender == 'u':
        return True
    else:
        print('Wrong gender: Please select either M, W or U')
        return False


def is_valid_amount(amount):
    try:
        value = int(amount)
        return True

    except ValueError:
        print('Invalid amount, please try again')
        return False


def is_valid_date(date):
    date_format = '%d/%m/%Y'

    try:
        datetime.datetime.strptime(date, date_format)
        return True

    except ValueError:
        print("Incorrect data input, date should be valid")
        return False


def handle_amount_input():
    while True:

        print('How many would you like to generate?')
        amount_input = input('> ')

        if amount_input == '':
            return '1'
        else:
            if is_valid_amount(amount_input):
                return '1' if int(amount_input) < 1 or int(amount_input) > 20 else amount_input


def handle_date_input():
    while True:

        print('Please fill in a valid DATE')
        date_input = input('> ')

        if date_input == '':
            return None
        else:
            if is_valid_date(date_input):
                return date_input


def handle_insz_gender():
    while True:

        print('For what gender would you like to generate?')
        gender_input = input('> ')

        if gender_input == '':
            return 'U'
        else:
            if is_valid_gender(gender_input):
                return gender_input.upper()


def check_number_generator(date, daily_serial):
    split_date = date.split('/')

    modulo_dividend_string = split_date[2][2:4] + split_date[1] + split_date[0] + daily_serial
    modulo_divisor_int = 97

    if split_date[2][0] == "2":
        modulo_result = int("2" + modulo_dividend_string) % modulo_divisor_int
        final_result = str(modulo_divisor_int - modulo_result)
        return final_result if len(final_result) > 1 else '0' + final_result
    else:
        modulo_result = int(modulo_dividend_string) % modulo_divisor_int
        final_result = str(modulo_divisor_int - modulo_result)
        return final_result if len(final_result) > 1 else '0' + final_result


def daily_serial_number_generator(gender):
    if gender.upper() == 'W':
        return '{}{}{}'.format(randint(0, 9), randint(0, 9), odd_number_generator(1, 9))
    elif gender.upper() == 'M':
        return '{}{}{}'.format(randint(0, 9), randint(0, 9), even_number_generator(0, 8))
    elif gender.upper() == 'U':
        return '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(1, 8))


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


def is_valid_insz_input(insz_input):
    modulo_divisor = 97

    if not insz_input.isnumeric() \
            or not len(insz_input) == 11:
        return False

    possible_pre_date = '{}/{}/19{}'.format(insz_input[4:6], insz_input[2:4], insz_input[0:2])
    possible_post_date = '{}/{}/20{}'.format(insz_input[4:6], insz_input[2:4], insz_input[0:2])

    input_check_number = int(insz_input[9:11])
    pre_2000_result = modulo_divisor - (int(insz_input[0:9]) % modulo_divisor)
    post_2000_result = modulo_divisor - (int('2' + insz_input[0:9]) % modulo_divisor)

    if (pre_2000_result == input_check_number and is_valid_date(possible_pre_date)) \
            or (post_2000_result == input_check_number and is_valid_date(possible_post_date)):
        return True


def handle_insz_input():
    while True:

        print('Please enter a valid INSZ number without symbols/space between numbers')
        insz_input = input('> ')

        if is_valid_insz_input(insz_input):
            return insz_input


def handle_date_year(insz_nr):
    modulo_divisor = 97
    check_number = insz_nr[9:11]
    pre_2000_result = modulo_divisor - (int(insz_nr[0:9]) % modulo_divisor)
    post_2000_result = modulo_divisor - (int('2' + insz_nr[0:9]) % modulo_divisor)

    if pre_2000_result == int(check_number):
        return False
    elif post_2000_result == int(check_number):
        return True


def print_error_message():
    print('Error while trying to generate a insz number, please make sure the query format is correct')
    print('An example of a correct query would be python insz.py 10/04/2003')
    print('You could also add an amount and gender to the query by appending the int and M/W')
    print('So if I wanted 5 female security numbers of a certain date it would look something like this:')
    print('python insz.py 10/04/2003 5 W')
    print('If no amount or gender is specified in the query, the default amount is 1 and genderless')


def print_options():
    print('1. Generate a BIS number')
    print('2. Generate a INSZ number')
    print('3. Decode a INSZ number')
    print('4. Exit')
