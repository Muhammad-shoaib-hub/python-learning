class BankAccount:
    bank_name = "Python National Bank"
    total_accounts = 0

    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self.balance = float(initial_balance)
        self.transactions = []
        self.transactions.append(f"Account opened with ${self.balance}")
        BankAccount.total_accounts += 1

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited ${amount}")
            print(f"Deposit successful! New balance: ${self.balance}")
        else:
            print("Transaction declined: Insufficient funds or invalid amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew ${amount}")
            print(f"Withdrawal successful! New balance: ${self.balance}")
        else:
            print("Transaction declined: Insufficient funds or invalid amount.")

    def get_statement(self):
        print(f"Owner: {self.account_holder}")
        print(f"Bank: {BankAccount.bank_name}")
        print(f"Current Balance: ${self.balance}")
        print("Transaction History:")
        for log in self.transactions:
            print(f" - {log}")


# Testing
account = BankAccount("Shoaib", 200)

account.deposit(100)
account.withdraw(50)
account.withdraw(500)   # should fail — not enough balance

account.get_statement()
print(f"Total accounts: {BankAccount.total_accounts}")