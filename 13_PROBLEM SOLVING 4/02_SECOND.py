#WRITE A PROGRAM TO CHECK IF THE NUMBER IS PRIME OR NOT
num=int(input("Eneter a number here"))
if num<=1:
    print("It is not a prime number")
else:
    for i in range (2,num):
        if num% i==0:
            print("Number is not a prime number")
            break
        else:
            print("It is a prime number")