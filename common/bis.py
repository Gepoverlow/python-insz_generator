from common import utility as u
from faker import Faker

fake = Faker()


def bis_generator(is_gender_known: bool, is_birthday_known: bool, date: str, amount: int) -> list[str]:
    generate_random_dates: bool = False
    bis_list: list[str] = list()

    if date is None:
        generate_random_dates = True

    for i in range(amount):
        if generate_random_dates is True:
            date: str = u.fake_date_generator()

        correct_date: str = u.date_refactorer_bis(date, is_gender_known, is_birthday_known)

        formatted_date: str = u.date_format_generator(correct_date)
        daily_serial: str = u.daily_serial_number_generator('U')
        check_number: str = u.check_number_generator(correct_date, daily_serial)

        bis_list.append(f'{formatted_date}{daily_serial}{check_number}')

    return bis_list


def bis_printer():
    while True:
        try:
            is_gender_known: bool = u.is_gender_known_input_handler()
            is_dob_known: bool = u.is_dob_known_input_handler()
            date: str = u.date_input_handler()
            amount: int = u.amount_input_handler()

            bis_results: list[str] = bis_generator(is_gender_known, is_dob_known, date, amount)

            for i in bis_results:
                print(i)
            break
        except IndexError:
            print('Something went wrong regarding an IndexError Exception')
        except ValueError:
            print('Something went wrong regarding an ValueError Exception')
        except TypeError:
            print('Something went wrong regarding an TypeError Exception')




