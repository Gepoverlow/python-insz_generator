import sys
import random
import datetime
import input_data_class
from random import randint


itemList = []

for i in range(1, len(sys.argv)):
    itemList.append(sys.argv[i])


inputData = input_data_class.InputData(*itemList)


def is_date(date):
    date_format = '%d/%m/%Y'

    try:
        datetime.datetime.strptime(date, date_format)
        return True

    except ValueError:
        print("Incorrect data input, should be a valid DD/MM/YYYY formatted date")
        return False


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


def date_format_generator(split_date):
    return split_date[2][2:4] + '.' + split_date[1] + '.' + split_date[0]


def print_error_message():
    print('Error while trying to generate a insz number, please make sure the query format is correct')
    print('An example of a correct query would be python main.py 10/04/2003')
    print('You could also add an amount and gender to the query by appending the int and M/W')
    print('So if I wanted 5 female security numbers of a certain date it would look something like this:')
    print('python main.py 10/04/2003 5 W')
    print('If no amount or gender is specified in the query, the default amount is 1 and genderless')


def insz_generator(data_obj):
    if not is_date(data_obj.date):
        return

    try:
        if int(data_obj.amount) < 1 or int(data_obj.amount) > 20:
            amount = 1
        else:
            amount = int(data_obj.amount)

        for i in range(amount):
            split_date = data_obj.date.split("/")

            formatted_date = date_format_generator(split_date)
            daily_serial = daily_serial_number_generator(data_obj.gender)
            check_number = check_number_generator(split_date, daily_serial)

            print(formatted_date + '-' + daily_serial + '.' + check_number)

    except IndexError:
        print_error_message()

    except ValueError:
        print_error_message()

    except TypeError:
        print_error_message()


insz_generator(inputData)
