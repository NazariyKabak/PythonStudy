class Car:
    def __init__(self, model):
        self.__model = model

    def go(self):
        print(f"{self.__model} go!")