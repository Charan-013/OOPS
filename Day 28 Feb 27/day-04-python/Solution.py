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
    
class LoanAccount(Account):
    def __init__(self, accountNumber, accountHolder, balance,interestRate):
        super().__init__(accountNumber, accountHolder, balance)
        self.loanAmount = balance
        self.interestRate = interestRate
    
    def repay(self,amount):
        if amount <= self.loanAmount:
            self.loanAmount = self.loanAmount - amount
    
    def calculateInterest(self):
        return self.loanAmount * self.interestRate
    
    def getOutstandingLoan(self):
        return self.loanAmount
    
class Bank:
    def __init__(self):
        self.accounts = []

    def addAccount(self,account):
        self.accounts.append(account)
    
    def findAccount(self,accountNumber):
        for account in self.accounts:
            if account.accountNumber == accountNumber:
                return account
        return 
    
    def transfer(self,fromAccountNum,toAccountNum,amount):
        A = self.findAccount(fromAccountNum)
        B = self.findAccount(toAccountNum)
        if A.withdraw(amount):
            B.deposit(amount)
            return True
        return False
    
class Person:
    def __init__(self,personID,name):
        self.personID = personID
        self.name = name
        self.accounts = []
        self.relationships = []

    def addAccount(self,account):
        self.accounts.append(account)

    def addRelationship(self,person):
        self.relationships.append(person)
    
    def getAccounts(self):
        return self.accounts
    
class Transaction:
    def __init__(self,transactionID,accountNumber,type,amount,transactionDate):
        self.transactionID = transactionID
        self.accountNumber = accountNumber
        self.type = type
        self.amount = amount
        self.transactionDate = transactionDate
        
    def __str__(self):
        return f"{self.transactionID} | {self.transactionDate} | {self.type} | {self.amount} | {self.accountNumber}"