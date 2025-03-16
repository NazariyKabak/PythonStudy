class NegativeNumError(Exception):

    def __init__(self, value):
        self.value = value
        super().__init__(f" Число {value} не може бути від'ємним!")


