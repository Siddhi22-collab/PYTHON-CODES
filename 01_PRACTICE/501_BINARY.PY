numbers = [2, 5, 7, 10, 15, 20, 25]
target = 15

left = 0
right = len(numbers) - 1

while left <= right:
    mid = (left + right) // 2

    if numbers[mid] == target:
        print("Element Found at index", mid)
        break
    elif numbers[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("Element Not Found")