# Write a Program to check the number fibonacci or not.
num = int(input("Enter a number: "))
a, b = 0, 1
is_fibo = False
while a <= num:
    if a == num:
        is_fibo = True
        break
    a, b = b, a + b
if is_fibo:
    print(num, "is a Fibonacci number.")
else:
    print(num, "is not a Fibonacci number.")
