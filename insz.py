import sys
import input_data_class
from util import is_valid_date, daily_serial_number_generator, check_number_generator, print_error_message


itemList = []

for i in range(1, len(sys.argv)):
    itemList.append(sys.argv[i])


inputData = input_data_class.InputData(*itemList)


def date_format_generator(split_date):
    return split_date[2][2:4] + '.' + split_date[1] + '.' + split_date[0]


def insz_generator(data_obj):
    if not is_valid_date(data_obj.date):
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
