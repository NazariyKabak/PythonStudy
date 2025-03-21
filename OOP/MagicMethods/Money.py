class Money:
    def __init__(self, amount):
        self.amount = int(amount)

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __str__(self):
        return f'{self.amount}'