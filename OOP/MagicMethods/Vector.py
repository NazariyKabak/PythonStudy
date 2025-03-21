class Vector:
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    def __str__(self):
        return f'({self.x}, {self.y})'
