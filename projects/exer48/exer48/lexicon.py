'''
 You want to take raw input from the user, carve it into words with split, analyze those words to identify their type, and finally make a sentence out of them.
 '''
 # part1: scanning input
'''
 # use this function to test if a input is a number
direction_words = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']

verbs = ['go', 'stop', 'kill', 'eat']

stop_words = ['the', 'in', 'of', 'from', 'at', 'it']

nouns = ['door', 'bear', 'princess', 'cabinet']
# numbers: any string of 0 through 9 characters??? how to handle this?

# how to trim the trailing period of one sentence?
def scan(input):
    input = input.split()
    sentence = []

    for word in input:
        if word in direction_words:
            tuple_word = ('direction', word)
        elif word in verbs:
            tuple_word = ('verb', word)
        elif word in stop_words:
            tuple_word = ('stop', word)
        elif word in nouns:
            tuple_word = ('noun', word)
        else:
            tuple_word = ('Error', word)

        sentence.append(tuple_word)

    return sentence
'''
# here is Zed's code:

lexicon = {
    'north': 'direction',
    'south': 'direction',
    'east': 'direction',
    'west': 'direction',
    'go': 'verb',
    'kill': 'verb',
    'eat': 'verb',
    'the': 'stop',
    'in': 'stop',
    'of': 'stop',
    'bear': 'noun',
    'princess': 'noun'
    }

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def scan(sentence):
    words = sentence.split()
    result = []

    for word in words:
        if word in lexicon.keys():
            pair = (lexicon[word], word)
            result.append(pair)
        elif convert_number(word) != None:
            pair = ('number', int(word))
            result.append(pair)
        else:
            pair = ('error', word)
            result.append(pair)

    return result
