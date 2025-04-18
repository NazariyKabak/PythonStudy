class RetailItem:
    def __init__(self, describe_product, count, price):
        self.__describe_product = describe_product
        self.__count = count
        self.__price = price

    def get_describe_product(self):
        return self.__describe_product

    def get_count(self):
        return self.__count

    def get_price(self):
        return self.__price

    def set_describe_product(self, describe_product):
        self.__describe_product = describe_product

    def set_count(self, count):
        self.__count = count

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return f"Product: {self.__describe_product}, Count: {self.__count}, Price: {self.__price}"

