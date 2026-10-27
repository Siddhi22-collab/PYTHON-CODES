def second_longest_word(sentence):
    words = sentence.split()

    unique_words = list(set(words))

    if len(unique_words) < 2:
        return "No second distinct word"

    longest = ""
    second = ""

    for word in unique_words:
        if len(word) > len(longest):
            second = longest
            longest = word

        elif len(word) > len(second) and word != longest:
            second = word

    return second


text = input("Enter a sentence: ")
print("Second longest word:", second_longest_word(text))