class InputData:
    def __init__(self, date, amount=None, gender=None):
        self.date = date
        if amount is None:
            self.amount = '1'
        else:
            self.amount = amount
        if gender is None:
            self.gender = 'U'
        else:
            self.gender = gender