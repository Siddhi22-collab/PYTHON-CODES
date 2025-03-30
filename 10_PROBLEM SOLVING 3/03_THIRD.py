#WRITE A PROGRAM TO FIND SUM OF FIRST 10 ODD NUMBER USING WHILE LOOP
sum=0
n=0
while n<=20:
    if n%2 !=0:
        sum +=n
        n+=1
        print("sum of first 10 odd number is",sum)