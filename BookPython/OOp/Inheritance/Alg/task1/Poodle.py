from BookPython.OOp.Inheritance.Alg.task1.Dog import Dog
class Poodle(Dog):
    def __init__(self, name, age, weight, haircut_style, competition_ready):
        super().__init__(name, age, "Poodle", weight)
        self.haircut_style = haircut_style  # стиль стрижки
        self.competition_ready = competition_ready # чи готується до виставки

