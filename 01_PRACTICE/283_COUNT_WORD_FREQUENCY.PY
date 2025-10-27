text = input("Enter a sentence: ")
words = text.split()
freq = {word: words.count(word) for word in set(words)}
print(freq)
