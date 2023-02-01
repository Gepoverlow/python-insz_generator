import sys
from random import randint


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


def daily_serial_number_generator():
    return '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(1, 8))


def date_format_generator(split_date):
    return split_date[2][2:4] + '.' + split_date[1] + '.' + split_date[0]


def insz_generator(date):
    try:
        split_date = date.split("/")

        formatted_date = date_format_generator(split_date)
        daily_serial = daily_serial_number_generator()
        check_number = check_number_generator(split_date, daily_serial)

        print(formatted_date + '-' + daily_serial + '.' + check_number)

    except IndexError:
        print('error while trying to generate a security number, please make sure the date format is correct')

    except ValueError:
        print('error while trying to generate a security number, please make sure the date format is correct')


for i in range(1, len(sys.argv)):
    insz_generator(sys.argv[i])
