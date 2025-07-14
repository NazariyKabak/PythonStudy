from BookPython.OOp.Inheritance.Alg.task3.beverage import Beverage


class Cola(Beverage):
    def __init__(self, cola_type):
        super().__init__("Coca- cola")
        self.__cola_type = cola_type

    def get_cola_type(self):
        return self.__cola_type

    def set_cola_type(self, cola_type):
        self.__cola_type = cola_type

