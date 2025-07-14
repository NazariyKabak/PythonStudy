class Person:
    def __init__(self, name, address, phone_number):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone_number(self):
        return self.__phone_number

    def __str__(self):
        return (f"Name: {self.get_name()}, Address: {self.get_address()}, "
                f"Phone: {self.get_phone_number()}, ID: {self.__id_client}, "
                f"Subscribed: {self.__notification}")
