n = int(input())
temp = n
sum1 = 0

while n > 0:
    digit = n % 10
    sum1 += digit ** 3
    n //= 10

if temp == sum1:
    print("Armstrong")
else:
    print("Not Armstrong")