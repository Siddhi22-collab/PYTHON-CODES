lst = [1, 2, 3, 4, 5]
k = int(input("Enter k: "))
k = k % len(lst)
rotated = lst[k:] + lst[:k]
print("Rotated list:", rotated)
