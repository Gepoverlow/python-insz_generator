from common import utility as u
from typing import List
from faker import Faker

fake = Faker()


def insz_generator(date: str, amount: int, gender: str) -> List[str]:
    is_random_dates: bool = False
    insz_list: list[str] = list()

    if date is None:
        is_random_dates = True

    for i in range(amount):
        if is_random_dates is True:
            date: str = u.fake_date_generator()

        formatted_date: str = u.date_format_generator(date)
        daily_serial: str = u.daily_serial_number_generator(gender)
        check_number: str = u.check_number_generator(date, daily_serial)

        insz_list.append(f'{formatted_date}{daily_serial}{check_number}')

    return insz_list


def insz_printer() -> None:
    while True:
        try:
            date: str = u.date_input_handler()
            amount: int = u.amount_input_handler()
            gender: str = u.gender_input_handler()

            insz_results: list[str] = insz_generator(date, amount, gender)

            for i in insz_results:
                print(i)
            break
        except IndexError:
            print('Something went wrong regarding an IndexError Exception')
        except ValueError:
            print('Something went wrong regarding an ValueError Exception')
        except TypeError:
            print('Something went wrong regarding an TypeError Exception')


def insz_decoder(insz_nr: str, is_post_2000_date: bool, gender: str) -> str:
    birth_day: str = insz_nr[4:6]
    birth_month: str = insz_nr[2:4]
    birth_year: str = '20' + insz_nr[0:2] if is_post_2000_date else '19' + insz_nr[0:2]

    return f'This persons birth day is {birth_day}-{birth_month}-{birth_year} and the gender is {gender}'


def insz_decode_printer() -> None:
    while True:
        try:
            insz: str = u.insz_input_handler()
            is_post_2000_date: bool = u.is_date_2000(insz)
            gender: str = u.insz_gender_detector(insz)

            decode_result: str = insz_decoder(insz, is_post_2000_date, gender)
            print(decode_result)
            break
        except IndexError:
            print('Something went wrong regarding an IndexError Exception')
        except ValueError:
            print('Something went wrong regarding an ValueError Exception')
        except TypeError:
            print('Something went wrong regarding an TypeError Exception')
