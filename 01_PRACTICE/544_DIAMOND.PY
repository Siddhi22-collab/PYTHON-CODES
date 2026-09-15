n = 5

# Upper half
for i in range(1, n + 1):

    # Print spaces
    for j in range(n - i):
        print(" ", end="")

    # Increasing numbers
    for j in range(1, i + 1):
        print(j, end="")

    # Decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()


# Lower half
for i in range(n - 1, 0, -1):

    # Print spaces
    for j in range(n - i):
        print(" ", end="")

    # Increasing numbers
    for j in range(1, i + 1):
        print(j, end="")

    # Decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()