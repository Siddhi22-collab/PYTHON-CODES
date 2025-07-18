
n = int(input("How many numbers? "))
max_num = float(input("Enter number 1: "))
for i in range(2, n + 1):
    num = float(input(f"Enter number {i}: "))
    if num > max_num:
        max_num = num
print("The greatest number is:", max_num)
