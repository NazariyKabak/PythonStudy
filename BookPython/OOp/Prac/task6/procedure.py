class Procedure:
    def __init__(self, name, date, name_doctor, price):
        self.__name = name
        self.__date = date
        self.__name_doctor = name_doctor
        self.__price = price

    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_name_doctor(self):
        return self.__name_doctor

    def get_price(self):
        return self.__price

    def set_name(self, name):
        self.__name = name

    def set_date(self, date):
        self.__date = date

    def set_name_doctor(self, name_doctor):
        self.__name_doctor = name_doctor

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return f"{self.__name} {self.__date} {self.__name_doctor} {self.__price}"