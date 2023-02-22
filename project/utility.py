import datetime
import random
from random import randint


def is_valid_gender(gender: str) -> bool:
    return True if gender.lower() in ['m', 'w', 'u'] else print('Wrong Input -> Pick between m, w or u')


def is_valid_amount(amount: str) -> bool:
    return True if amount.isdigit() else print('Invalid amount, please input a number')


def is_valid_date(date: str) -> bool:
    date_format: str = '%d/%m/%Y'

    try:
        datetime.datetime.strptime(date, date_format)
        return True

    except ValueError:
        print("Incorrect data input, date should be valid")


def is_valid_yes_or_no_input(gender_known: str) -> bool:
    return True if gender_known.lower() in ['y', 'n'] else print('Wrong Input -> Pick between y or n')


def is_valid_insz_input(insz_input: str) -> bool:
    if not insz_input.isnumeric() \
            or not len(insz_input) == 11:
        return False

    possible_pre_date: str = '{}/{}/19{}'.format(insz_input[4:6], insz_input[2:4], insz_input[0:2])
    possible_post_date: str = '{}/{}/20{}'.format(insz_input[4:6], insz_input[2:4], insz_input[0:2])

    input_check_number: int = int(insz_input[9:11])
    pre_2000_result: int = 97 - (int(insz_input[0:9]) % 97)
    post_2000_result: int = 97 - (int('2' + insz_input[0:9]) % 97)

    if (pre_2000_result == input_check_number and is_valid_date(possible_pre_date)) \
            or (post_2000_result == input_check_number and is_valid_date(possible_post_date)):
        return True


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
        return '{}{}{}'.format(randint(0, 9), randint(0, 9), odd_number_generator(1, 9))
    elif gender.upper() == 'W':
        return '{}{}{}'.format(randint(0, 9), randint(0, 9), even_number_generator(0, 8))
    elif gender.upper() == 'U':
        return '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(1, 8))


def handle_amount_input() -> str:
    while True:

        print('How many would you like to generate?')
        amount_input: str = input('> ')

        if amount_input == '':
            return '1'
        else:
            if is_valid_amount(amount_input):
                return '1' if int(amount_input) < 1 or int(amount_input) > 20 else amount_input


def handle_date_input() -> None or str:
    while True:

        print('Please fill in a valid DATE')
        date_input: str = input('> ')

        if date_input == '':
            return None
        else:
            if is_valid_date(date_input):
                return date_input


def handle_insz_gender_input() -> str:
    while True:

        print('For what gender would you like to generate?')
        gender_input: str = input('> ')

        if gender_input == '':
            return 'U'
        else:
            if is_valid_gender(gender_input):
                return gender_input.upper()


def handle_bis_is_gender_known_input() -> bool:
    while True:

        print('Is the gender known?')
        gender_known_input: str = input('> ')

        if gender_known_input == '':
            return True
        else:
            if is_valid_yes_or_no_input(gender_known_input):
                return True if gender_known_input.lower() == 'y' else False


def handle_bis_is_birthday_known_input() -> bool:
    while True:

        print('Is the birthday known?')
        birthday_known_input: str = input('> ')

        if birthday_known_input == '':
            return True
        else:
            if is_valid_yes_or_no_input(birthday_known_input):
                return True if birthday_known_input.lower() == 'y' else False


def handle_insz_input() -> str:
    while True:

        print('Please enter a valid INSZ number without symbols/space between numbers')
        insz_input: str = input('> ')

        if is_valid_insz_input(insz_input):
            return insz_input


def date_refactorer_bis(date: str, is_gender_known: str, is_birthday_known: str) -> str:
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
