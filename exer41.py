import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object): \n\tdef __init__(self, ***)":
      "class %%% has-a __init__ function that takes self and *** parameters.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip()) # .strip() is the function in list class? what for? remove what character?


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))] # <---- this is just to make the first letter of the sentence Uppercase~~~
    # list comprehension!!!!!

    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(",".join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:] # don't understand this part
        '''
        That's a Python way of copying a list. You're using the list slice syntax [:] to effectively make a slice from the very first element to the very last one.
        '''

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)
        # fake other names:
        for word in other_names:
            result = result.replace("***", word, 1)
        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)
    return results

# keep going until they hit CTRL-D
try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase) # the function defined by previous part!, get the results

            if PHRASE_FIRST:
                question, answer = answer, question

            print question

            raw_input("> ")
            print "Answer: %s\n\n" % answer

except EOFError: # <------ when hit control-D
    print "\nBye"
