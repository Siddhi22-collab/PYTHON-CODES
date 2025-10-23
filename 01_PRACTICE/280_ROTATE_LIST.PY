def rotate_left(lst, k):
    # Handle cases where k > len(lst)
    k = k % len(lst)
    return lst[k:] + lst[:k]

# Example usage
numbers = [10, 20, 30, 40, 50]
k = 2

rotated_list = rotate_left(numbers, k)
print("Original list:", numbers)
print(f"List rotated left by {k} positions:", rotated_list)
