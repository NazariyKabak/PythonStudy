class Book:
    def __init__(self, title, author, price):
        self.__title = title
        self.__author = author
        self.__price = price


    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_price(self):
        return self.__price

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_price(self, price):
        self.__price = price

    def print_book(self):
        print(self.__title)
        print(self.__author)
        print(self.__price)