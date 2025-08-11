class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance  

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

account = BankAccount("Siddhi", 5000)
print(account.balance)
account.deposit(2000)
account.withdraw(1000)
print(account.balance)
