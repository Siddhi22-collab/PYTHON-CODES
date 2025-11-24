from itertools import permutations

items = [1, 2, 3]
perms = list(permutations(items))

print("Permutations:")
for p in perms:
    print(p)
