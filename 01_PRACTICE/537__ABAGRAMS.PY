str1 = "listen"
str2 = "silent"

if len(str1) != len(str2):
    print("Not Anagram")
else:
    frequency = {}

    for char in str1:
        frequency[char] = frequency.get(char, 0) + 1

    for char in str2:
        frequency[char] = frequency.get(char, 0) - 1

    is_anagram = True

    for value in frequency.values():
        if value != 0:
            is_anagram = False
            break

    if is_anagram:
        print("Anagram")
    else:
        print("Not Anagram")