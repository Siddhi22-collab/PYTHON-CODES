#WRITE A PROGRAM TO CHECK IF A STRING IS PALINDROME
A=input("Enter anything here:")
rev=A[::-1]
if A==rev:
    print("It is a palindrme")
else:
    print("It is not a palindrme")