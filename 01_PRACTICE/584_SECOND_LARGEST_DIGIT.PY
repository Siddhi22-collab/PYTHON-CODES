num = input("Enter a number: ")
digits = set(num.lstrip("-"))

if len(digits) < 2:
    print("Second-largest digit does not exist")
else:
    digits = sorted(digits, reverse=True)
    print("Second-largest digit:", digits[1])