
a = int(input("Enter first positive number: "))
b = int(input("Enter second positive number: "))

if a <= 0 or b <= 0:
    print("Invalid input")
else:
    small = a

    if b < small:
        small = b

    while small > 0:
        if a % small == 0 and b % small == 0:
            print("GCD:", small)
            break

        small -= 1
