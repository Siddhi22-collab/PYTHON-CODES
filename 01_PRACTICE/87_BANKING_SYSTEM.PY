class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: ${amount}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew: ${amount}"

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: ${self.balance}"

# Usage
acc = BankAccount("Alice", 1000)
print(acc.deposit(500))
print(acc.withdraw(300))
print(acc)