# regular expressions

import re
# re.search(Pat, Text)
# it returns a match object


def Find(pat, text):
    match = re.search(pat, text) # powerful function to search...
    if match:
        print match.group()
        print match.group(1) # group 1 refers to the left most ()
        print match.group(2) # group 2 is the next () ...
    else:
        print 'Not Found.'

def Findall(pat, text):
    match = re.findall(pat, text) # here it is a list object
    ### also, if the pattern has () in it, then in the list that will be tuples!!!!
    if match:
        print match
    else:
        print 'Not found'



import sys

def main():
    if len(sys.argv) != 4 and len(sys.argv) != 3:
        print 'usage: ./day_2_part_1.py {--search | --findall} pattern file'
        sys.exit(1)
    option = sys.argv[1]
    pat = sys.argv[2]
    text  = sys.argv[3]
    if option == '--search':
        Find(pat, text)
    elif option == '--findall':
        Findall(pat, text)
    else:
        print 'unknown option: ' + option
        sys.exit(1)


if __name__ == '__main__':
  main()


##### dir(re) will show all the options for re.
## .all will return all characters, .* will go to the next file...
# for example:
# re.findall(r'([\w.]+)@([\w.]+)', 'blah blah blah blah nick.p@gmail.com    foo@bar    ', re.I) <-- this will ignore upper and lower case difference in the text...

# write to the file
# file = open(filename, 'w')
# file.write(some other text) <---- this will write texts to that file...