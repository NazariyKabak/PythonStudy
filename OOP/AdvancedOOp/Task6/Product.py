from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    @abstractmethod
    def get_info(self):
        pass

    def get_price(self):
        return self.price
