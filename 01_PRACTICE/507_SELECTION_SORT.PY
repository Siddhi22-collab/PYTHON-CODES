arr = [64, 25, 12, 22, 11]

n = len(arr)

for i in range(n):
    min_index = i

    # Find the smallest element
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    # Swap the smallest element with the current position
    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted Array:", arr)