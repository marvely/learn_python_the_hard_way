# ++++++++++ Parser ++++++++++++++++ #
# what we want is to turn the above lists of tuples into a nice Sentence object that has subject, verb and object.

# Exception is error detected during execution.
class ParserError(Exception):
    pass
# this is the base class for exceptions in this module


'''
to do this, we need four tools:
    1. a way to loop through the list of scanned words
    2. a way to match different types of tuples that we expect in our Subject Verb Object setup
    3. a way to 'peek' at a potential tuple so we can make some decisions
    4. a way to 'skip' things we do not care about, like stop words
    5. a sentence object to put the results in

'''
# use peek() to look at the next element in our tuple list, and then match to take one off and work with it

class Sentence(object):

    def __init__(self, subject, verb, obj):
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

# Returns the first element of the word_list.
def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0] # <--- get the category of the word
    else:
        return None

# Pop the first element of the word_list, if the first word of the first element equals expecting, returns the first element, otherwise return none.
def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0) # <--- just get the 1st element off the list

        if word[0] == expecting:
            return word # <---- still returns the tuple
        else:
            return None

    else:
        return None


def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)
    #return word_list
    # if i don't put any return in this function, it will not return any, even it has return in match, it won't affect the
#### i don't get this piece of code...... why is this?


# first, we scan the verb:
def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError('Expected a verb next.')

def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError('Expected a noun or direction next.')

def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player') #<---- player is implied
    else:
        raise ParserError('Expected a verb next.')

def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)
