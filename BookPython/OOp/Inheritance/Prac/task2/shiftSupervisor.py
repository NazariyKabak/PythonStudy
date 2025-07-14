from BookPython.OOp.Inheritance.Prac.task1.employee import Employee


class ShiftSupervisor(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name)
        self.__salary = salary
        self.__bonus = bonus

    def get_annual_salary(self):
        return self.__annual_salary

    def set_annual_salary(self, salary):
        self.__annual_salary = salary

    def get_annual_bonus(self):
        return self.__annual_bonus

    def set_annual_bonus(self, bonus):
        self.__annual_bonus = bonus

