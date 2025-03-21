from OOP.AdvancedOOp.Task7.Account import Account


class BankAccount(Account):
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.add_transaction(f"💰 Депозит: +{amount} грн")
            print(f"✅ Поповнено на {amount} грн")
        else:
            print("Невірна сума!")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Недостатньо коштів або невірна сума")
        else:
            self._balance -= amount
            self.add_transaction(f"💸 Зняття: -{amount} грн")
            print(f"✅ Знято {amount} грн")
