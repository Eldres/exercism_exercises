import string

def is_pangram(sentence):
    letter_included = lambda letter: letter in sentence.lower()
    has_letters = map(letter_included, string.ascii_lowercase)
    return all(has_letters)
