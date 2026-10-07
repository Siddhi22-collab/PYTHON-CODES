n = 5

for i in range(1, n + 1):
    # Print spaces
    for j in range(n - i):
        print(" ", end="")

    # Print stars
    for j in range(1, 2 * i):
        if i == n or j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print()