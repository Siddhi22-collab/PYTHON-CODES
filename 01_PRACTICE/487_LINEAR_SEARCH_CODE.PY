arr = [10, 25, 30, 45, 50]

key = int(input("Enter element: "))

for i in range(len(arr)):
    if arr[i] == key:
        print("Found at index", i)
        break
else:
    print("Not Found")