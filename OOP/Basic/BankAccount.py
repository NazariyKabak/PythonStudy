class BankAccount:
    def __init__(self, balance):
        self.__balance = balance



    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Сума поповнення має бути більше 0.")


    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError
        elif amount > 0:
            self.__balance -= amount
        else:
            print("❌ Некоректна сума для зняття.")

    def set_balance(self, balance):
        if balance > self.__balance:
            raise ValueError
        else:
            self.__balance = balance
    def get_balance(self):
        return self.__balance
