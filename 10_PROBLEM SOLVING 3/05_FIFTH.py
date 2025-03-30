#WRITE A PROGRAM TO CREATE A BILLING SYSTEM AT SUPERMARKET
while True:
    name=input("enter customers name:")
    total=0
    while True:
        print("Enter the amount and quantity")
        amount=float(input("Enter amount:"))
        quantity=float(input("Enter quantity:"))
        total += amount*quantity
        repeat=input("do you want add more item?(yes/no):")
        if repeat=='no' or repeat=='NO':
            break
        print("-"*40)
        print("Name:",name)
        print("amount to be paid:",total)
        print("-"*40)
        repeat=input("do you want add more item?(yes/no):")
        if repeat=='no' or repeat=='NO':
            break