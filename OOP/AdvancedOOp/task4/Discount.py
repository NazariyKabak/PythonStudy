class Discount:
    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.price * 0.1
