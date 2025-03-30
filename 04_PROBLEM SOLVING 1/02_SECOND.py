#WRITE A PROGRAM TO SWAP A TWO VARIABLE
#METHOD 1
a=12
b=13
temp=a
print(temp)
a=b
print(a)
b=temp
print(b)
print("Value of a is:",a)
print("Value of b is:",b)

#METHOD 2
a=10
b=20
#left,right=right,left
a,b=b,a
print(b)
print(a)