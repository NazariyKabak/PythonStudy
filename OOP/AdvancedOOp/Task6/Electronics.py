from OOP.AdvancedOOp.Task6.Product import Product


class Electronics(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand

    def get_info(self):
        return f"{self.brand} {self.name} - {self.price} грн"

