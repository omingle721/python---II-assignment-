class BankAccount:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Current balance:", self.balance)


# Creating object
account1 = BankAccount(12345, 5000)

# Operations
account1.deposit(2000)
account1.withdraw(1500)
account1.check_balance()