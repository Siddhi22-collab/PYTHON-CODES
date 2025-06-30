# 16. Find second largest element
arr = [12, 35, 1, 10, 34, 1]
unique = list(set(arr))
unique.sort()
print("Second largest:", unique[-2])

# 17. Remove duplicates
arr = [1, 2, 2, 3, 4, 4, 5]
arr = list(set(arr))
print("After removing duplicates:", arr)

# 18. Merge two arrays
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
merged = arr1 + arr2
print("Merged:", merged)
