li=[2*e for e in range(1,10)]
print(li)
li2=[e for e in li if e%3==0]   
print(li2)
li3=[e for e in li if e%3!=0]
print(li3)
li4=[e for e in li if e%3==0 and e%5==0]
print(li4)