# ++++++++++++++++++++++++++++++++++++++++++++++++++ #
'''
from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %s" % filename
print txt.read()
txt.close()

print "Type the filename again:"
file_again = raw_input("> ")
txt_again = open(file_again)

print txt_again.read()
txt_again.close() # <------- it is important to close the file too!
'''

# ++++++++++++++++++++++++++++++++++++++++++++++++++ #
from sys import argv
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, "w")

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "Im going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
