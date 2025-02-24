class BankAccount:
    def __init__(self,accountNumber,balance,accountType):
        self.accountNumber = accountNumber
        self.balance = balance
        self.accountType = accountType
    
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
        else:
            return False
        
    def withdraw(self,amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            return False

    def getBalance(self):
        return self.balance
    

class Customer:

    def __init__(self,customerID,name,accounts):
        self.customerID = customerID
        self.name = name
        self.accounts = accounts

    def addAccount(self,account):
        self.accounts.append(account)
    
    def getAccount(self,accountNumber):
        for ele in self.accounts:
            # print(ele.accountNumber,accountNumber)
            if ele.accountNumber == accountNumber:
                # print("done")
                return ele
        return False




def main():
    # Create a BankAccount and test deposit/withdrawal
    account = BankAccount("ACC001", 1000.0, "savings")
    account.deposit(500.0)
    if account.getBalance() != 1500.0:
        print("Error: Incorrect balance after deposit.")
    # Test valid withdrawal
    success_withdraw = account.withdraw(300.0)
    print("Withdrawal of 300 successful:", success_withdraw)
    # Test invalid withdrawal (exceeding balance)
    fail_withdraw = account.withdraw(2000.0)
    print("Withdrawal of 2000 (should fail):", fail_withdraw)
    # Create a Customer and add the account
    customer = Customer(1, "John Doe", [])
    customer.addAccount(account)
    retrieved = customer.getAccount("ACC001")
    print("Retrieved account balance:", retrieved.getBalance())
    # Test retrieval of a non-existing account
    non_exist = customer.getAccount("ACC999")
    print("Non-existent account retrieval:", non_exist is None)
if __name__ == '__main__':
    main()