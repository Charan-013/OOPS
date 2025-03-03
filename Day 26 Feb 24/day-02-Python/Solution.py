class Account:
    def __init__(self,accountNumber,accountHolder,balance):
        self.accountNumber = accountNumber
        self.accountHolder = accountHolder
        self.balance = balance
    
    def deposit(self,amount):
        if amount > 0:self.balance += amount
    
    def withdraw(self,amount):
        if amount < self.balance:
            self.balance = self.balance - amount
            return True
        return False

    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self,accountNumber,accountHolder,balance,interestRate):
        super().__init__(accountNumber,accountHolder,balance)
        self.interestRate = interestRate
    
    def calculateInterest(self):
        return self.balance * self.interestRate

class CurrentAccount(Account):
    def __init__(self,accountNumber,accountHolder,balance,overdraftLimit):
        super().__init__(accountNumber,accountHolder,balance)
        self.overdraftLimit = overdraftLimit

    def withdraw(self, amount):
        if amount < self.balance + self.overdraftLimit:
            self.balance = self.balance - amount
            return True
        return False