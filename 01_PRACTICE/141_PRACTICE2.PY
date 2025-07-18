# Write a program to check if a number is armstrong or not.
num = int(input("Enter a number: "))
num_digits = len(str(num))
sum_of_powers = sum(int(digit) ** num_digits for digit in str(num))
if num == sum_of_powers:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
