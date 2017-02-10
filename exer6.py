# ++++++++++++++++ string +++++++++++++++++++++++ #
'''
Strings may contain the format characters you have discovered so far. You simply put the formatted variables in the string, and then a % (percent) character, followed by the variable.
'''
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x # <-------- here we did not use the single qoute but in the result there are!!!!! why????

print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" #<------ use %r for dbugging since it displaces the RAW data.

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."
print w + e

# +++++++++++++++++++++++++++++++++++++++++++++++ #
print "Kary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Kary went."
print "." * 10 # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

# ++++++++++++++++++++++++++++++++++++++++++++++++++ #
# put anything into %r

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)

print formatter % (
  "I had this thing.",
  "That you could type up right.",
  "But it didn't sing.",
  "So I said goodnight."
)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++ #
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"  #<----- \n begins a new line

print "Here are the days: ", days
print "Here are the months: ", months

print '''
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
'''

# +++++++++++++++++++++++++++++++++++++++++++++++++++ #
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# fun code to try
#while True:
#    for i in ["/", "-", "|", "\\", "|"]:
#        print "%s\r" %i,
# how can i stop it??????

# +++++++++++++++++++++++++++++++++++++++++++++++++++ #
print "How old are you?"
age = raw_input()
print "How tall are you?"
height = raw_input()
print "How much do you weight?"
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++ #
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How muchb do you weight? ")

print "So, you're %r old, %s tall and %r heavy." % (age, height, weight)
