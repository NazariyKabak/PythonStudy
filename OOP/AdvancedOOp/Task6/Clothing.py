from OOP.AdvancedOOp.Task6.Product import Product


class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.__size = size

    def get_info(self):
        return f"{self.name} (Size: {self.__size}) - {self.price} грн"