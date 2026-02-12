def first_repeating(arr):
    seen = set()

    for num in arr:
        if num in seen:
            return num
        seen.add(num)

    return None


print(first_repeating([10, 5, 3, 4, 3, 5, 6]))
