#WRITE A PROGRAM TO FIND NUMBER OF VOWELS IN A STRING
A=input("Enter anything here:")
vowels=0
for i in A:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        vowels+=1
        break
    print("THE NUMBER OF VOWELS IN THE FOLLOWING STRING ARE:",vowels)    
