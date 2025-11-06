def vowel_frequency(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    s_vowels = set(vowels)
    s_sentence = set(sentence.lower())
    print(s_vowels, s_sentence)
    return s_vowels.intersection(s_sentence)

# sentence = "The quick brown fox jumps over the lazy dog"
# print(vowel_frequency(sentence))


def find_key_words(sentence, word_list):
    s_sentence = set(sentence.lower().split())
    print(s_sentence)
    s_word_list = set(word_list)
    print(s_word_list)
    return s_word_list.intersection(s_sentence)

sentence = "The quick brown fox jumps over the lazy dog"
word_list = ["the", "dog"]
print(find_key_words(sentence, word_list))