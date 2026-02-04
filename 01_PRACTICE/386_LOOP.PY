start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

even = []
odd = []
total_even = 0
total_odd = 0

for i in range(start, end + 1):
    if i % 2 == 0:
        even.append(i)
        total_even += i
    else:
        odd.append(i)
        total_odd += i

print("Even numbers:", even)
print("Total is:", total_even)

print("Odd numbers:", odd)
print("Total is:", total_odd)
