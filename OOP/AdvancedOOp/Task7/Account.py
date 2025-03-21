from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, owner, balance):
        self._owner = owner
        self._balance = balance
        self._transactions = []

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def check_balance(self):
        return self._balance

    def add_transaction(self, transaction):
        self._transactions.append(transaction)

    def history_transactions(self):
        print(f"📜 Історія транзакцій для {self._owner}:")
        for transaction in self._transactions:
            print(transaction)
