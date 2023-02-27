from common.utility import \
    daily_serial_number_generator, \
    check_number_generator, \
    date_format_generator,\
    date_refactorer_bis,\
    handle_date_input,\
    handle_amount_input,\
    handle_is_gender_known_input,\
    handle_is_dob_known_input

from faker import Faker

fake = Faker()


def handle_bis_generation(is_gender_known: bool, is_birthday_known: bool, date: str, amount: int) -> list[str]:
    generate_random_dates: bool = False
    bis_list: list[str] = list()

    if date is None:
        generate_random_dates = True

    for i in range(amount):
        if generate_random_dates is True:
            split_random_date: list[str] = str(fake.date()).split('-')
            date: str = '{}/{}/{}'.format(split_random_date[2], split_random_date[1], split_random_date[0])

        correct_date: str = date_refactorer_bis(date, is_gender_known, is_birthday_known)

        formatted_date: str = date_format_generator(correct_date)
        daily_serial: str = daily_serial_number_generator('U')
        check_number: str = check_number_generator(correct_date, daily_serial)

        bis_list.append('{}{}{}'.format(formatted_date, daily_serial, check_number))

    return bis_list


def generate_bis():
    while True:
        try:
            is_gender_known: bool = handle_is_gender_known_input()
            is_dob_known: bool = handle_is_dob_known_input()
            date: str = handle_date_input()
            amount: int = handle_amount_input()

            bis_results: list[str] = handle_bis_generation(is_gender_known, is_dob_known, date, amount)

            for i in bis_results:
                print(i)
            break
        except:
            print('Something went wrong')
            break




