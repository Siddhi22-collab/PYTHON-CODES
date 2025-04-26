vowels = 'aeiouAEIOU'
string = input("Enter a string: ")
count = 0

for char in string:
    if char in vowels:
        count += 1

print(f"There are {count} vowels in the string.")