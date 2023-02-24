import datetime
import random
from random import randint


def is_valid_gender(gender: str) -> bool:
    return True if gender.lower() in ['m', 'w', 'u'] else print('Invalid gender input, please pick between m, w or u')


def is_valid_amount(amount: str) -> bool:
    return True if amount.isdigit() else print('Invalid amount input, please select a valid amount')


def is_valid_date(date: str) -> bool:
    date_format: str = '%d/%m/%Y'

    try:
        datetime.datetime.strptime(date, date_format)
        return True

    except ValueError:
        print("Invalid date input, please select a valid date")


def is_valid_yes_or_no_input(gender_known: str) -> bool:
    return True if gender_known.lower() in ['y', 'n'] else print('Invalid input, please pick between y or n')


def is_valid_insz_input(insz_input: str) -> bool:
    if not insz_input.isnumeric() \
            or not len(insz_input) == 11:
        print('Invalid insz input, please pick a valid insz number')
        return False

    possible_pre_date: str = '{}/{}/19{}'.format(insz_input[4:6], insz_input[2:4], insz_input[0:2])
    possible_post_date: str = '{}/{}/20{}'.format(insz_input[4:6], insz_input[2:4], insz_input[0:2])

    input_check_number: int = int(insz_input[9:11])
    pre_2000_result: int = 97 - (int(insz_input[0:9]) % 97)
    post_2000_result: int = 97 - (int('2' + insz_input[0:9]) % 97)

    if (pre_2000_result == input_check_number and is_valid_date(possible_pre_date)) \
            or (post_2000_result == input_check_number and is_valid_date(possible_post_date)):
        return True

    else:
        print('Invalid insz, please pick a valid insz number')


def is_2000_date(insz_nr: str) -> bool:
    check_number: str = insz_nr[9:11]
    post_2000_check_nr: int = 97 - (int('2' + insz_nr[0:9]) % 97)

    return True if post_2000_check_nr == int(check_number) else False


def odd_number_generator() -> str:
    return random.choice([i for i in range(1, 9 + 1) if i % 2 != 0])


def even_number_generator() -> str:
    return random.choice([i for i in range(0, 8) if i % 2 == 0])


def date_format_generator(date: str) -> str:
    split_date: list[str] = date.split("/")

    return split_date[2][2:4] + '.' + split_date[1] + '.' + split_date[0]


def check_number_generator(date: str, daily_serial: str) -> str:
    split_date: list[str] = date.split('/')
    year: int = int(split_date[2])

    modulo_dividend_string: str = split_date[2][2:4] + split_date[1] + split_date[0] + daily_serial

    if year >= 2000:
        modulo_result: int = int("2" + modulo_dividend_string) % 97

    else:
        modulo_result: int = int(modulo_dividend_string) % 97

    final_result: str = str(97 - modulo_result)
    return final_result if len(final_result) > 1 else '0' + final_result


def daily_serial_number_generator(gender: str) -> str:
    if gender.upper() == 'M':
        return '{}{}{}'.format(randint(0, 9), randint(0, 9), odd_number_generator())

    elif gender.upper() == 'W':
        return '{}{}{}'.format(randint(0, 9), randint(0, 9), even_number_generator())

    elif gender.upper() == 'U':
        return '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(1, 8))


def handle_amount_input() -> int:
    while True:

        amount_input = input('How many would you like to generate? > ')

        if amount_input == '':
            amount_input = 1
            break

        elif is_valid_amount(amount_input):
            if int(amount_input) < 1 or int(amount_input) > 20:
                amount_input = 1
            break

        else:
            continue

    return int(amount_input)


def handle_date_input() -> None or str:
    while True:

        date_input = input('Please fill in a valid DATE > ')

        if date_input == '':
            date_input = None
            break

        elif is_valid_date(date_input):
            break

        else:
            continue

    return date_input


def handle_insz_gender_input() -> str:
    while True:

        gender_input: str = input('For what gender would you like to generate? > ')

        if gender_input == '':
            gender_input = 'U'
            break

        elif is_valid_gender(gender_input):
            break

        else:
            continue

    return gender_input


def handle_is_gender_known_input() -> bool:
    while True:

        gender_known_input: str = input('Is the gender known? > ')
        is_gender_known: bool = True

        if gender_known_input == '':
            break

        elif is_valid_yes_or_no_input(gender_known_input):
            if gender_known_input.lower() == 'n':
                is_gender_known = False
            break

        else:
            continue

    return is_gender_known


def handle_is_dob_known_input() -> bool:
    while True:

        dob_known_input: str = input('Is the date of birth known? > ')
        is_dob_known: bool = True

        if dob_known_input == '':
            break

        elif is_valid_yes_or_no_input(dob_known_input):
            if dob_known_input.lower() == 'n':
                is_dob_known = False
            break

        else:
            continue

    return is_dob_known


def handle_insz_input() -> str:
    while True:

        insz_input = input('Please enter a valid INSZ number without symbols/space between numbers > ')

        if is_valid_insz_input(insz_input):
            break

        else:
            continue

    return insz_input


def date_refactorer_bis(date: str, is_gender_known: bool, is_birthday_known: bool) -> str:
    split_date: list[str] = date.split("/")

    if is_gender_known is True and is_birthday_known is True:
        return '{}/{}/{}'.format(split_date[0], str(int(split_date[1]) + 40), split_date[2])

    elif is_gender_known is False and is_birthday_known is True:
        return '{}/{}/{}'.format(split_date[0], str(int(split_date[1]) + 20), split_date[2])

    elif is_gender_known is True and is_birthday_known is False:
        return '{}/{}/{}'.format('0' + str(random.randint(0, 3)), '40', split_date[2])

    else:
        return '{}/{}/{}'.format('0' + str(random.randint(0, 3)), '20', split_date[2])


def detect_insz_gender(insz_nr: str) -> str:
    daily_serial_number: str = insz_nr[6:9]

    return 'Female' if int(daily_serial_number[2]) % 2 == 0 else 'Male'


def print_error_message() -> None:
    print('Error while trying to generate a insz number, please make sure the query format is correct')
    print('An example of a correct query would be python insz.py 10/04/2003')
    print('You could also add an amount and gender to the query by appending the int and M/W')
    print('So if I wanted 5 female security numbers of a certain date it would look something like this:')
    print('python insz.py 10/04/2003 5 W')
    print('If no amount or gender is specified in the query, the default amount is 1 and genderless')


def print_options() -> None:
    print('1. Generate a BIS number')
    print('2. Generate a INSZ number')
    print('3. Decode a INSZ number')
    print('4. Exit')
