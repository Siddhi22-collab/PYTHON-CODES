#WRITE A PROGRAM TO CHECK THE NUMBER IS PALINDROME OR NOT
num=int(input("Enter a number here:"))
temp=num
rev=0
while num>0:
    dig=num%0
    rev=rev*10+dig
    num=num//10
    if rev==temp:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")