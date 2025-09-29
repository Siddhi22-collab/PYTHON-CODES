text = "Python Programming"
vowels = "aeiouAEIOU"
count = sum(1 for ch in text if ch in vowels)
print("Vowel count:", count)