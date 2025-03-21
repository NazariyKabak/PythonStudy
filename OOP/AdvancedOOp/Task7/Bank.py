from OOP.AdvancedOOp.Task7.BankAccount import BankAccount
from OOP.AdvancedOOp.Task7.VIPBankAccount import VIPBankAccount


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, owner, acc_type="regular"):
        if acc_type == "regular":
            self.accounts[owner] = BankAccount(owner)
        elif acc_type == "vip":
            self.accounts[owner] = VIPBankAccount(owner)

        print(f"🏦 Рахунок {acc_type.upper()} для {owner} відкрито!")

    def get_account(self, owner):
        return self.accounts.get(owner, None)
