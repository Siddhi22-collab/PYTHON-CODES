def find_sum(numbers):
    total = 0  
    for num in numbers:
        total += num
    return total

nums = [1, 2, 3, 4, 5]
print("Sum:", find_sum(nums))
