class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise NegativeAmountException("Deposit amount cannot be negative.")

    def withdraw(self, amount):
        if amount < 0:
            raise NegativeAmountException("Withdrawal amount cannot be negative.")
        elif amount <= self.balance:
            self.balance -= amount
        else:
            raise InsufficientFundsException("Insufficient funds for withdrawal.")

    def get_balance(self):
        return self.balance


class InsufficientFundsException(Exception):
    def __init__(self, message):
        self.message = message


class NegativeAmountException(Exception):
    def __init__(self, message):
        self.message = message
