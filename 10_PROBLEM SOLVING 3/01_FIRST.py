#WRITE A PROGRAM TO FIND A SUM OF ALL EVEN NUMBER UPTO 50
sum=0
for i in range (1,51):
    if i%2==0:
        sum +=i
        print("Sum of all even number upto 50 is",sum) 