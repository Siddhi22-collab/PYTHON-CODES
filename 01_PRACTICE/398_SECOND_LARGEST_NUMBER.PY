def second_largest(lst):
    first = second = float('-inf')
    for num in lst:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second

nums = [10, 20, 4, 45, 99]
print("Second Largest:", second_largest(nums))
