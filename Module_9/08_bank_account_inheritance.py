from Module_4.h_04_cashmachine_while import account_balance


class BankAccount:
    def __init__(self):
        self.account_balance = 1000

    def deposit(self, amount: int):
        self.account_balance += amount

    def withdraw(self, amount: int):
        if self.account_balance <= amount:
            return 0

        self.account_balance -= amount

class SavingsAccount(BankAccount):
    def __init__(self, savings: int = 0.1):
        super().__init__()
        self.savings = savings

    def collect_savings(self):
        self.deposit(self.savings * self.amount)

def test_account():
    account_balance = BankAccount()
    account.deposit(100000)
    account.withdraw(50000)
    assert account_balance.amount == 50000


