# +++++++++++ list ++++++++++++++++ #
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() # so it's going backward!!!!! and taking things off this list!!!
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff
print "What happened to more_stuff?", more_stuff

print "Let's do some things with stuff."

print stuff[1]

print stuff[-1] # whoa! fancy

print stuff.pop() # <------ i never understand this function .pop() means the last one?

print " ".join(stuff) # what? cool!

print "#".join(stuff[3:5]) # super stellar!
