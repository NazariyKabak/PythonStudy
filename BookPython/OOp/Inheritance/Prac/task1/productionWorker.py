from BookPython.OOp.Inheritance.Prac.task1.employee import Employee
class ProductionWorker(Employee):
    def __init__(self,name, id, shift_number,hourly_rate):
        super().__init__(name, id)
        self.__shift_number = shift_number
        self.__hourly_rate = hourly_rate

    def work_shift_definition(self):
        if self.__shift_number == 1:
            print("Day shift")
        else:
            print("Night shift")

    def get_name(self):
        return super().get_name()
    def get_id(self):
        return super().get_id()
    def get_shift_number(self):
        return self.__shift_number
    def get_hourly_rate(self):
        return self.__hourly_rate

    def set_hourly_rate(self, hourly_rate):
        self.__hourly_rate = hourly_rate

    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def __str__(self):
        print("Name:", self.__name, "id:", self.__id, "shift_number:", self.__shift_number, "hourly_rate:", self.__hourly_rate)