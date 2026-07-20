arr = [10, 20, 30, 20, 40, 50, 30, 60]

duplicate = []

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j] and arr[i] not in duplicate:
            duplicate.append(arr[i])

print(duplicate)