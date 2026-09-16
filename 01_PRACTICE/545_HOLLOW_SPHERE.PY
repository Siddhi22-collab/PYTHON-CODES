n = 7

for i in range(n):
    for j in range(n):
        distance = (i - n//2)**2 + (j - n//2)**2

        if distance >= (n//2)**2 - 2 and distance <= (n//2)**2 + 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()