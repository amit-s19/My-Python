""" Creating a small python library """

def break_words(stuff):
    """ This Function breaks the para into tokens"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """ This function sorts the words """
    return sorted(words)

def print_first_word(words):
    """ This function prints the first word of the sentence """
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """ This function prints the last word of the sentence """
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """ Takes in a full sentence and returns the sorted words """
    words = break_words(sentence)
    return sorted(words)

def print_first_and_last(sentence):
    """ This function prints the first and last word the sentence """
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
