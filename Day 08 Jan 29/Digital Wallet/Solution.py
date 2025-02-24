class DigiWallet:
    def __init__(self):
        self.bal = 0.0
        self.transHistory = []

    def init_wallet(self):
        self.bal = 0.0
        self.transHistory = []
        print(f"Wallet initialized with balance 0 and empty transaction history.")

    def display_TheBalance(self):
        print(f"Current balance: {self.bal}")

    def add_TheFunds(self, value):
        if value <= 0:
            print(f"Invalid amount. Transaction not recorded.")
        else:
            self.bal += value
            self.transHistory.append(value)

            print(f"Balance updated to {self.bal}, transaction history logged.")

    def make_ThePayment(self, value):
        temp_bal = self.bal - value
        if temp_bal < 0:
            print(f"Insufficient balance. Transaction not recorded.")
            return

        self.bal -= value
        self.transHistory.append(-value)
        print(f"Balance updated to {self.bal}, transaction history logged.")

    def view_TheTransationHistory(self):
        trans = [f"{x:.1f}" for x in self.transHistory]
        print("[", end="")
        for ele in trans:
            temp = ele
            ele = float(ele)
            if ele > 0 and trans.index(temp) != len(trans) - 1:
                print(f"+{ele}", end=", ")
            elif ele > 0 and trans.index(temp) == len(trans) - 1:
                print(f"+{ele}", end="")
            elif ele < 0 and trans.index(temp) != len(trans) - 1:
                print(f"{ele}", end=", ")
            elif ele < 0 and trans.index(temp) == len(trans) - 1:
                print(f"{ele}", end="")
            elif ele == 0 and trans.index(temp) != len(trans) - 1:
                print(ele, end=", ")
            elif ele == 0 and trans.index(temp) == len(trans) - 1:
                print(ele)
        print("]")

    def run_TheWallet(self):
        while True:
            try:
                inp = input().strip()
                if not inp:
                    break

                if inp.startswith("Method:"):
                    method_name = inp.split(":")[1].strip()
                    value = input().strip()

                    if method_name == "initialize_wallet":
                        self.init_wallet()
                    elif method_name == "add_funds":
                        value = value.strip().split("Inputs: amount=")
                        # print(value[1])
                        self.add_TheFunds(int(value[1]))
                    elif method_name == "make_payment":
                        value = value.strip().split("Inputs: amount=")
                        self.make_ThePayment(int(value[1]))
                    elif method_name == "view_transaction_history":
                        self.view_TheTransationHistory()
                    elif method_name == "display_balance":
                        self.display_TheBalance()
                    else:
                        print("Invalid method name.")
                else:
                    print("Invalid input format. Please start with 'Method:'")
            except EOFError:
                break


if __name__ == "__main__":
    digiWalet = DigiWallet()
    digiWalet.run_TheWallet()
