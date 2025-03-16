import math

from OOP.Basic.Shape import Shape


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * math.pi