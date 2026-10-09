numbers = [1, 2, 2, 3, 1, 1, 4]

visited = []

for i in range(len(numbers)):

    if numbers[i] in visited:
        continue

    frequency = 0

    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            frequency += 1

    print(numbers[i], "→", frequency)

    visited.append(numbers[i])