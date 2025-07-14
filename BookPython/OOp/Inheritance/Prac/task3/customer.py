from BookPython.OOp.Inheritance.Prac.task3.person import Person


class Customer(Person):
    def __init__(self, name, address, phone_number, id_client, notification):
        super().__init__(name, address, phone_number)
        self.__id_client = id_client
        self.__notification = notification

    def get_id_client(self):
        return self.__id_client

    def get_notify(self):
        return self.__notification

    def set_id_client(self, id_client):
        self.__id_client = id_client

    def set_notification(self, notification):
        self.__notification = notification

    def __str__(self):
        return f"ID: {self.__id_client}, Notify: {self.__notification}"