class Product:
    def __init__(self, type, price):
        self.type = type
        self.price = price

    def __eq__(self, other):
        return self.type == other.type and self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

    def __str__(self):
        return f'{self.type} {self.price}'