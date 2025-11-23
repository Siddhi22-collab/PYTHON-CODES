from itertools import permutations

items = ['A', 'B', 'C']

# generate all permutations of length 3
perm_list = list(permutations(items, 3))

print("All permutations:")
for p in perm_list:
    print(p)
