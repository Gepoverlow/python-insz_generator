from common import utility as u

import hug


@hug.type(extend=hug.types.number)
def amount_type(value):
    if value < 1 or value > 20:
        raise ValueError('Amount provided can be a minimum of 1 or a maximum of 20')
    return value


@hug.type(extend=hug.types.text)
def gender_type(value):
    if not u.is_gender_valid(value):
        raise ValueError('Gender provided is not valid, please select between m, w or u')
    return value


@hug.type(extend=hug.types.text)
def date_type(value):
    if not u.is_date_valid(value):
        raise ValueError('Date provided is not valid')
    return value

