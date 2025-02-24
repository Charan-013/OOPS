class Transaction:
    def __init__(self):
        self.type = ""
        self.amount = 0
        self.fee = 0

    def initilize(self, type1, amount, fee):
        self.type = type1
        self.amount = amount
        self.fee = fee

        return f"{self.type} {self.amount} (Fee: {self.fee})"


class Wallet:
    def __init__(self):
        self.balance = 0.0
        self.transactions = []
        self.withdrawLimit = 0
        self.withdrawlFeePercentage = 0.0

    def deposite(self, amount):
        if amount < 0:
            # print(f"Deposit of {amount} failed. Balance remains: {self.balance}")
            return False
        else:
            self.balance += amount
            # print(f"Deposit of {amount} successful. Current balance: {self.balance}")
            self.transactions.append(Transaction.initilize(self, "DEPOSIT", amount, float(0.0)))
            return True

    def withdraw(self, amount):
        fee = self.withdrawlFeePercentage * (1 / 100) * amount
        temp = self.balance - amount
        if temp < 0 or amount > self.withdrawLimit:
            # print(f"Withdrawal of {amount} failed. Balance remains: {self.balance}")
            return False
        else:
            self.balance -= amount
            self.balance -= fee
            # print(f"Withdrawal of {amount} successful with a fee of {fee}. Current balance: {self.balance}")
            self.transactions.append(Transaction.initilize(self, "WITHDRAW", amount, fee))
            return True

    def get_Balance(self):
        return self.balance
        # print(f"Current Balance: {self.balance}")

    def get_Transactions(self):
        return self.transactions
        # print(f"Transaction History:")
        # for i in range(len(self.transactions)):
        #     print(f"{i+1}. {self.transactions[i]}")


def digital_Wallet():
    wallet = Wallet()
    transaction = Transaction()
    while True:
        try:
            inp = input().strip()

            if not inp:
                break

            if inp.startswith("deposit "):
                inp = inp.split("deposit ")
                amount = float(inp[1])
                if wallet.deposite(amount):
                    print(f"Deposit of {amount} successful. Current balance: {wallet.balance}")
                    transaction.initilize("DEPOSIT", amount, float(0.0))
                else:
                    print(f"Deposit of {amount} failed. Balance remains: {wallet.balance}")

            elif inp.startswith("withdraw "):
                inp = inp.split("withdraw ")
                amount = float(inp[1])
                fee = wallet.withdrawlFeePercentage * (1 / 100) * amount
                if wallet.withdraw(amount):
                    print(f"Withdrawal of {amount} successful with a fee of {fee}. Current balance: {wallet.balance}")
                else:
                   print(f"Withdrawal of {amount} failed. Balance remains: {wallet.balance}") 
                    
            elif inp.startswith("getBalance"):
                print(f"Current Balance: {wallet.get_Balance()}")

            elif inp.startswith("getTransactions"):
                l = wallet.get_Transactions()
                print(f"Transaction History:")
                for i in range(len(l)):
                    print(f"{i+1}. {l[i]}")
            else:
                inp = inp.split(" ")
                wallet.withdrawLimit = float(inp[0])
                wallet.withdrawlFeePercentage = float(inp[1])
                # print(wallet.balance)
                # print(wallet.withdrawlFeePercentage)
                print(f"Wallet initialized with withdrawalLimit: {float(inp[0])}, withdrawalFeePercentage: {float(inp[1])}%")
        except EOFError:
            break


if __name__ == "__main__":
    digitalwallet = digital_Wallet()
    digital_Wallet()
