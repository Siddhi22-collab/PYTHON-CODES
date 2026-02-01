a= int(input("Enter a number: "))

if a % 2 == 0 and a % 3 == 0:
    print("Divisible by 2 and 3")
elif a % 2 == 0 and a % 3 != 0:
    print("Divisible by 2 but not divisible by 3")
elif a % 3 == 0 and a % 2 != 0:
    print("Divisible by 3 but not divisible by 2")
else:
    print("Not divisible by 2 and not divisible by 3")