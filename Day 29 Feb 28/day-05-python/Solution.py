
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
        # if amount <= self.loanAmount:
        self.loanAmount = self.loanAmount - amount
    
    def calculateInterest(self):
        return self.loanAmount * self.interestRate
    
    def getOutstandingLoan(self):
        return self.loanAmount
    
class Bank:
    def __init__(self):
        self.accounts = []
        self.transactions = []

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
    
    def logTransaction(self, transaction):
        self.transactions.append(transaction)
    
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
    
def createPerson():
    personID = input("Enter person ID: ")
    name = input("Enter person name: ")
    person = Person(personID, name)
    return person

def createAccount(bank, person):
    print("\nChoose account type:")
    print("1. Savings Account")
    print("2. Current Account")
    print("3. Loan Account")
    
    choice = int(input("Enter your choice: "))
    accountNumber = input("Enter account number: ")
    balance = float(input("Enter initial balance: "))
    
    if choice == 1:
        interestRate = float(input("Enter interest rate: "))
        account = SavingsAccount(accountNumber, person, balance, interestRate)
    elif choice == 2:
        overdraftLimit = float(input("Enter overdraft limit: "))
        account = CurrentAccount(accountNumber, person, balance, overdraftLimit)
    elif choice == 3:
        interestRate = float(input("Enter loan interest rate: "))
        account = LoanAccount(accountNumber, person, balance, interestRate)
    else:
        print("Invalid choice!")
        return None
    
    person.addAccount(account)
    bank.addAccount(account)
    return account

def deposit(account):
    amount = float(input("Enter amount to deposit: "))
    if account.deposit(amount):
        print(f"Deposit successful! New balance: {account.getBalance()}")
    else:
        print("Invalid deposit amount.")

def withdraw(account):
    amount = float(input("Enter amount to withdraw: "))
    if account.withdraw(amount):
        print(f"Withdrawal successful! New balance: {account.getBalance()}")
    else:
        print("Insufficient funds or invalid withdrawal amount.")

def transfer(bank):
    fromAccountNum = input("Enter source account number: ")
    toAccountNum = input("Enter destination account number: ")
    amount = float(input("Enter amount to transfer: "))
    if bank.transfer(fromAccountNum, toAccountNum, amount):
        print(f"Transfer successful!")
    else:
        print("Transfer failed. Check account balances or account numbers.")

def repayLoan(account):
    if isinstance(account, LoanAccount):
        amount = float(input("Enter loan repayment amount: "))
        account.repay(amount)
        print(f"Repayment successful! Outstanding loan amount: {account.getOutstandingLoan()}")
    else:
        print("This is not a Loan Account.")

def displayMenu():
    print("\nMenu:")
    print("1. Create Person")
    print("2. Create Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Transfer")
    print("6. Repay Loan")
    print("7. Exit")

def main():
    bank = Bank()
    person = None
    
    while True:
        displayMenu()
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            person = createPerson()
            print(f"Person created: {person.name} (ID: {person.personID})")
        elif choice == 2:
            if person is None:
                print("Create a person first!")
                continue
            createAccount(bank, person)
        elif choice == 3:
            if person is None or not person.getAccounts():
                print("No accounts available for deposit!")
                continue
            accountNumber = input("Enter account number to deposit to: ")
            account = bank.findAccount(accountNumber)
            if account:
                deposit(account)
            else:
                print("Account not found.")
        elif choice == 4:
            if person is None or not person.getAccounts():
                print("No accounts available for withdrawal!")
                continue
            accountNumber = input("Enter account number to withdraw from: ")
            account = bank.findAccount(accountNumber)
            if account:
                withdraw(account)
            else:
                print("Account not found.")
        elif choice == 5:
            transfer(bank)
        elif choice == 6:
            if person is None or not person.getAccounts():
                print("No loan accounts available!")
                continue
            accountNumber = input("Enter loan account number to repay: ")
            account = bank.findAccount(accountNumber)
            if account:
                repayLoan(account)
            else:
                print("Account not found.")
        elif choice == 7:
            print("Exiting the banking system.")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()