#WRITE A PROGRAM TO CHECK IF A NUMBER IS DIVISIBLE BY 8 AND 12 UPTO 100 NUMBER
for i in range(1,101):
    if i%8==0 and i%12==0:
        print(i)
    