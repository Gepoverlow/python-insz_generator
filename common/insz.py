from common.utility import \
    daily_serial_number_generator, \
    check_number_generator, \
    date_format_generator, \
    handle_date_input, \
    handle_amount_input, \
    handle_insz_gender_input, \
    handle_insz_input, \
    is_2000_date, \
    detect_insz_gender

from faker import Faker

fake = Faker()


def handle_insz_generation(date: str, amount: int, gender: str) -> list[str]:
    generate_random_dates: bool = False
    insz_list: list[str] = list()

    if date is None:
        generate_random_dates = True

    for i in range(amount):
        if generate_random_dates is True:
            split_random_date: list[str] = str(fake.date()).split('-')
            date: str = '{}/{}/{}'.format(split_random_date[2], split_random_date[1], split_random_date[0])

        formatted_date: str = date_format_generator(date)
        daily_serial: str = daily_serial_number_generator(gender)
        check_number: str = check_number_generator(date, daily_serial)

        insz_list.append('{}{}{}'.format(formatted_date, daily_serial, check_number))

    return insz_list


def generate_insz() -> None:
    while True:
        try:
            date: str = handle_date_input()
            amount: int = handle_amount_input()
            gender: str = handle_insz_gender_input()

            insz_results: list[str] = handle_insz_generation(date, amount, gender)

            for i in insz_results:
                print(i)
            break
        except:
            print('Something went wrong')
            break


def handle_insz_decodification(insz_nr: str, is_post_2000_date: bool, gender: str) -> str:
    birth_day: str = insz_nr[4:6]
    birth_month: str = insz_nr[2:4]
    birth_year: str = '20' + insz_nr[0:2] if is_post_2000_date else '19' + insz_nr[0:2]

    return 'This persons birth day is {}/{}/{} and the gender is {}'.format(birth_day,
                                                                            birth_month,
                                                                            birth_year,
                                                                            gender)


def decode_insz() -> None:
    while True:
        try:
            insz: str = handle_insz_input()
            is_post_2000_date: bool = is_2000_date(insz)
            gender: str = detect_insz_gender(insz)

            decode_result: str = handle_insz_decodification(insz, is_post_2000_date, gender)
            print(decode_result)
            break
        except:
            print('Something went wrong')
            break
