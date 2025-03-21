from OOP.AdvancedOOp.task4.Discount import Discount


class VIPDiscount(Discount):
    def __init__(self, price):
        super().__init__(price)

    def get_price(self):
        return self.price * 0.5
