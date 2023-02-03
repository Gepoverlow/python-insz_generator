import datetime
import random
from random import randint


def is_date(date):
    date_format = '%d/%m/%Y'

    try:
        datetime.datetime.strptime(date, date_format)
        return True

    except ValueError:
        print("Incorrect data input, should be a valid DD/MM/YYYY formatted date")
        return False


def odd_number_generator(n_from, n_to):
    return random.choice([i for i in range(n_from, n_to + 1) if i % 2 != 0])


def even_number_generator(n_from, n_to):
    return random.choice([i for i in range(n_from, n_to) if i % 2 == 0])


def daily_serial_number_generator(gender):
    if gender.upper() == 'W':
        return '{}{}{}'.format(randint(0, 9), randint(0, 9), odd_number_generator(1, 9))
    elif gender.upper() == 'M':
        return '{}{}{}'.format(randint(0, 9), randint(0, 9), even_number_generator(0, 8))
    elif gender.upper() == 'U':
        return '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(1, 8))


def check_number_generator(split_date, daily_serial):
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
    print('3. Exit')
