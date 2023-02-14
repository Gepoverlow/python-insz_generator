from general_util import daily_serial_number_generator, check_number_generator
from faker import Faker

fake = Faker()


def handle_insz_generation(date, amount, gender):
    generate_random_dates = False

    if date is None:
        generate_random_dates = True

    for i in range(int(amount)):
        if generate_random_dates is True:
            split_random_date = str(fake.date()).split('-')
            date = '{}/{}/{}'.format(split_random_date[2], split_random_date[1], split_random_date[0])

        formatted_date = date_format_generator_insz(date)
        daily_serial = daily_serial_number_generator(gender)
        check_number = check_number_generator(date, daily_serial)

        print(formatted_date + '-' + daily_serial + '.' + check_number)

