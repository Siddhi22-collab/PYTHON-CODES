#WRITE A PROGRAM TO CHECK IF A NUMBER IS A SINGLE DIGIT NUMBER, 2 DIGIT NUMBER OR SO ON UPTO 5 DIGIT NUMBER
num=int(input("Enter a number here upto five digit"))
if num>=0 and num<=9:
    print("it is a single digit number")
elif num>=10 and num<=99:
    print("it is a two digit number")
elif num>=100 and num<=999:
    print("it is a three digit number")
elif num>=1000 and num<=9999:
    print("it is a four digit number")
else:
    print("it is a five digit number")