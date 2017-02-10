def break_words(stuff):
    '''This function will break up words for us.'''
    words = stuff.split(' ')
    return words # <- still a temporary variable that needs to be assigned to a global variable out there~

def sort_words(input_words):
    '''Sort the inputed words'''
    return sorted(input_words)

def print_first_word(input_words):
    '''Print the first word after popping it off.'''
    first_word = input_words.pop(0) # <---- what is this function do?
    print first_word

def print_last_word(input_words):
    '''Print the last word after popping it off.'''
    last_word = input_words.pop(-1) # <------- ???
    print last_word

def sort_sentence(sentence):
    '''Takes in a full sentence and returns the sorted words.'''
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    '''Prints the first and last words of the sentence'''
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    '''Sorts the words then prints the first and last one'''
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
