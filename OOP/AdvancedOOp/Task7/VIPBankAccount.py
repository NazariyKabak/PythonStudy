from OOP.AdvancedOOp.Task7.Account import Account
from OOP.AdvancedOOp.Task7.BankAccount import BankAccount


class VIPBankAccount(BankAccount):

    def __init__(self, owner, balance = 0, overdraft_limit = 5000):
        super().__init__(owner, balance)
        self.__overdraft = overdraft_limit

    def withdraw(self, amount):
        if amount <= self._balance + self.__overdraft:
            self._balance -= amount
            self.add_transaction(f"💸 Зняття (овердрафт): -{amount} грн")
            print(f"✅ Знято {amount} грн (з урахуванням овердрафту)")
        else:
            print("❌ Недостатньо коштів навіть з овердрафтом")
