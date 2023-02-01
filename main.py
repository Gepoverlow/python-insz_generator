import sys
import random
from random import randint


class InputData:
    def __init__(self, date, amount=None, gender=None):
        self.date = date
        if amount is None:
            self.amount = '1'
        else:
            self.amount = amount
        if gender is None:
            self.gender = 'U'
        else:
            self.gender = gender


itemList = []

for i in range(1, len(sys.argv)):
    itemList.append(sys.argv[i])

inputData = InputData(*itemList)


def check_number_generator(split_date, daily_serial):
    modulo_dividend_string = split_date[2][2:4] + split_date[1] + split_date[0] + daily_serial
    modulo_divisor_int = 97

    if split_date[2][0] == "2":
        result_after_mod = int("2" + modulo_dividend_string) % modulo_divisor_int
        final_result = str(modulo_divisor_int - result_after_mod)
        return final_result if len(final_result) > 1 else '0' + final_result
    else:
        result_after_mod = int(modulo_dividend_string) % modulo_divisor_int
        final_result = str(modulo_divisor_int - result_after_mod)
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


def insz_generator(data_obj):
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
        print('error while trying to generate a security number, please make sure the date format is correct')

    except ValueError:
        print('error while trying to generate a security number, please make sure the date format is correct')

    except TypeError:
        print('error while trying to generate a security number, please make sure the date format is correct')


insz_generator(inputData)
