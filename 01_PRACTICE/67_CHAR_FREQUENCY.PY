text = "medium level practice"
freq = {}

for char in text:
    if char != ' ':
        freq[char] = freq.get(char, 0) + 1

print(freq)
