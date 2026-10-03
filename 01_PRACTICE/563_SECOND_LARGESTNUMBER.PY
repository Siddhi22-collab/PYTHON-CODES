numbers = [10, 45, 20, 89, 45, 67, 89, 30]

largest = float('-inf')
second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

if second_largest == float('-inf'):
    print("Second-largest distinct number does not exist")
else:
    print("Largest number:", largest)
    print("Second-largest number:", second_largest)