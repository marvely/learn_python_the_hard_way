# ++++++++ object oriented programming +++++++ #
mystuff = {'apple': "I am apples!"}
print mystuff['apple']

# modules are like dictionary!!!

import mystuff # <---- I've created a file called mystuff. And here I can import it to use the function I def inside it!
mystuff.apple()
print mystuff.tangerine

# how modules are similar to dictionary, but the syntax is different

'''
This means we have a very common pattern in Python:
1. Take a key=value stype container.
2. Get something out of it by the key's name.
'''
class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between" #<--- setting tangerine instance variable.
# this function let the class to create things based on itself.
# and you can set up anything in the init function

    def apple(self):
        print "I am Classy apples!"
############# difference between a class and a module: ###################
# if you create a class, you can make crafts based on one class and use it million times in one program, and each one of them won't interfere with each other.
# when you import a module there is only one for the entire program unless you do some monster hacks..... hahaha monster hacks...

# +++++++++++ understand what "OBJECT" is +++++++++++++++++++ #
'''
If a class is like a "mini-module", then there has to be a silimar concept to import but for classes.
That's "instantiate", which is basically "create".
'''
# instantiate:
thing = MyStuff() #<--- Python crafts an empty object with all the functions you've specified in the class using def.
# Python looks for __init__, and if you have it in the class, then Python uses it to initialize your newly created empty object.
# self is the empty object that Python made for me!

thing.apple()
print thing.tangerine

# class is used as a blueprint for building a copy of that type of thing.
# the resulting created mini-module is called an object and you then assign it to a variable to work with it.

# +++++++++++++++ first class example +++++++++++++++++++++ #
class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

# self is for clarification of the attribute. without self, lyrics = lyrics is ambiguous. with self, self.lyrics is clearly the instance attribute.

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_b_day = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I will stop right there"])
bulls_on_parade = Song(["They rally around the family",
                       "with pockets full of shells"])

print "can I get this? ", happy_b_day.lyrics
happy_b_day.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

# ++++++++++ manipulate the lyrics and variables ++++++++++++++++ #
# I want to create a dictionary and throw in all the song objects and then print them out.
album = dict()
album['happy_b_day'] = happy_b_day.lyrics
album['bulls_on_parade'] = bulls_on_parade.lyrics
print album
