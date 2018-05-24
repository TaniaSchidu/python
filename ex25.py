def break_words(stuff):
    """This function will break up words for us."""
    # split or breakup a string and add the data to a string array using a defined separator
    #if no separator is defined when you call upon the function, whitespace will be used by default
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    # sorted() method sorts the elements of a given iterable(sequence (string, tuple, list)
    # or collection(set, dictionary,frozen set) in a specific order (asc or desc)
    return sorted(words)

def print_first_word(words):
    # pop()method removes and returns the element at a given index (passed as an argument) from a list
    # pop(0) - the first element
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    #If no parameter is passed, th edefault index -1 is passed as an argument which returns the last element
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and the last words of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and the last one"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

