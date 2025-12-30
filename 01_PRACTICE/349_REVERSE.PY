def reverse_words(input_str):
    return ' '.join(word[::-1] for word in input_str.split())