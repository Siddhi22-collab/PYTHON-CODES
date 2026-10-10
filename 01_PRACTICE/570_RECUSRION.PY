def count(n,jumps):
    if n==0:
        return 1
    total = 0
    for j in jumps:
        if n-j >= 0:
            total += count(n-j,jumps)
    return total
print(count(4,[1,2,3]))