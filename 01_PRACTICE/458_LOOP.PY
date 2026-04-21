numbers=(34,54,67,21,78,97,45,44,80,19)
total=0
for i in numbers:
    print(total,'+',i,'=',end=' ')
    total=i+total
    print(total)
    
print("total =",total)