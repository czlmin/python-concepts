def unique_words(text):
    words = text.lower().split()
    words = set(words)
    number_of_unique_words = len(words)
    return number_of_unique_words

text = "Apple banana apple Orange orange"
print(unique_words(text))