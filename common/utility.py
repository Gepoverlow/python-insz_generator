import datetime
import random
from random import randint


def is_gender_valid(gender: str) -> bool:
    return True if gender.lower() in ['m', 'w', 'u'] else print('Invalid gender input, please pick between m, w or u')


def is_amount_valid(amount: str) -> bool:
    return True if amount.isdigit() else print('Invalid amount input, please select a valid amount')


def is_date_valid(date: str) -> bool:
    date_format: str = '%d/%m/%Y'

    try:
        datetime.datetime.strptime(date, date_format)
        return True

    except ValueError:
        print('Invalid date input, please select a valid date')


def is_yes_or_no_valid(gender_known: str) -> bool:
    return True if gender_known.lower() in ['y', 'n'] else print('Invalid input, please pick between y or n')


def is_insz_valid(insz: str) -> bool:
    err_message: str = 'Invalid insz input, please pick a valid insz number'

    if not insz.isnumeric() \
            or not len(insz) == 11:
        print(err_message)
        return False

    possible_pre_date: str = f'{insz[4:6]}/{insz[2:4]}/19{insz[0:2]}'
    possible_post_date: str = f'{insz[4:6]}/{insz[2:4]}/20{insz[0:2]}'

    input_check_number: int = int(insz[9:11])
    pre_2000_result: int = 97 - (int(insz[0:9]) % 97)
    post_2000_result: int = 97 - (int('2' + insz[0:9]) % 97)

    if (pre_2000_result == input_check_number and is_date_valid(possible_pre_date)) \
            or (post_2000_result == input_check_number and is_date_valid(possible_post_date)):
        return True

    else:
        print(err_message)
        return False


def is_date_2000(insz_nr: str) -> bool:
    check_number: str = insz_nr[9:11]
    post_2000_check_nr: int = 97 - (int('2' + insz_nr[0:9]) % 97)

    return True if post_2000_check_nr == int(check_number) else False


def odd_number_generator() -> str:
    return random.choice([i for i in range(1, 9 + 1) if i % 2 != 0])


def even_number_generator() -> str:
    return random.choice([i for i in range(0, 8) if i % 2 == 0])


def date_format_generator(date: str) -> str:
    split_date: list[str] = date.split("/")

    return f'{split_date[2][2:4]}{split_date[1]}{split_date[0]}'


def check_number_generator(date: str, daily_serial: str) -> str:
    date_split: list[str] = date.split('/')
    year: int = int(date_split[2])

    modulo_dividend: str = date_split[2][2:4] + date_split[1] + date_split[0] + daily_serial

    if year >= 2000:
        modulo_result: int = int("2" + modulo_dividend) % 97

    else:
        modulo_result: int = int(modulo_dividend) % 97

    final_result: str = str(97 - modulo_result)
    return final_result if len(final_result) > 1 else '0' + final_result


def daily_serial_number_generator(gender: str) -> str:
    first_nr: str = str(randint(0, 9))
    second_nr: str = str(randint(0, 9))

    if gender.lower() == 'm':
        third_nr: str = odd_number_generator()

    elif gender.lower() == 'w':
        third_nr: str = even_number_generator()

    elif gender.lower() == 'u':
        third_nr: str = str(randint(0, 9))

    return string_formatter(first_nr, second_nr, third_nr)


def amount_input_handler() -> int:
    while True:

        amount_input: str = input('How many would you like to generate? > ')

        if amount_input == '':
            amount_input = '1'
            break

        elif is_amount_valid(amount_input):
            if int(amount_input) < 1 or int(amount_input) > 20:
                amount_input = '1'
            break

        else:
            continue

    return int(amount_input)


def date_input_handler() -> None or str:
    while True:

        date_input: str or None = input('Please fill in a valid DATE > ')

        if date_input == '':
            date_input = None
            break

        elif is_date_valid(date_input):
            break

        else:
            continue

    return date_input


def gender_input_handler() -> str:
    while True:

        gender_input: str = input('For what gender would you like to generate? > ')

        if gender_input == '':
            gender_input = 'U'
            break

        elif is_gender_valid(gender_input):
            break

        else:
            continue

    return gender_input


def is_gender_known_input_handler() -> bool:
    while True:

        gender_known_input: str = input('Is the gender known? > ')
        is_gender_known: bool = True

        if gender_known_input == '':
            break

        elif is_yes_or_no_valid(gender_known_input):
            if gender_known_input.lower() == 'n':
                is_gender_known = False
            break

        else:
            continue

    return is_gender_known


def is_dob_known_input_handler() -> bool:
    while True:

        dob_known_input: str = input('Is the date of birth known? > ')
        is_dob_known: bool = True

        if dob_known_input == '':
            break

        elif is_yes_or_no_valid(dob_known_input):
            if dob_known_input.lower() == 'n':
                is_dob_known = False
            break

        else:
            continue

    return is_dob_known


def insz_input_handler() -> str:
    while True:

        insz_input: str = input('Please enter a valid INSZ number without symbols/space between numbers > ')

        if is_insz_valid(insz_input) is True:
            break

        else:
            continue

    return insz_input


def date_refactorer_bis(date: str, is_gender_known: bool, is_birthday_known: bool) -> str:
    split_date: list[str] = date.split("/")

    day: str = split_date[0]
    month: str = split_date[1]
    year: str = split_date[2]
    random_day: str = f'0{random.randint(0, 3)}'

    if is_gender_known is True and is_birthday_known is True:
        return date_string_formatter(day, int(month) + 40, year)

    elif is_gender_known is False and is_birthday_known is True:
        return date_string_formatter(day, int(month) + 20, year)

    elif is_gender_known is True and is_birthday_known is False:
        return date_string_formatter(random_day, '40', year)

    else:
        return date_string_formatter(random_day, '20', year)


def insz_gender_detector(insz_nr: str) -> str:
    daily_serial_number: str = insz_nr[6:9]

    return 'Female' if int(daily_serial_number[2]) % 2 == 0 else 'Male'


def string_formatter(a: str, b: str, c: str):
    return f'{a}{b}{c}'


def date_string_formatter(a: str, b: str or int, c: str):
    return f'{a}/{b}/{c}'


def print_options() -> None:
    print(' --------------------------- ')
    print('1. Generate a BIS number')
    print('2. Generate a INSZ number')
    print('3. Decode a INSZ number')
    print('4. Exit')
