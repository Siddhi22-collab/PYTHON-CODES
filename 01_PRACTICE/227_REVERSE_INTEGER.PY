def reverse(x):
    sign = -1 if x < 0 else 1
    x *= sign
    rev = int(str(x)[::-1])
    return 0 if rev > 2**31-1 else sign * rev

print(reverse(123))   # 321
print(reverse(-123))  # -321
