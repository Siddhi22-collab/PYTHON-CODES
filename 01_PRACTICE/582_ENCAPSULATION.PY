class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance


account = BankAccount("Rahul", 5000)

account.deposit(2000)
account.withdraw(1500)
print("Final balance:", account.get_balance())