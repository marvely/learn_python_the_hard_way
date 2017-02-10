# +++++++++++++++++ Evil Inheritance +++++++++++++++++++++++++ #
'''
Inheritance is used to indicate that one class will get most or all of its features from a parent class.
This happens implicitly whenever you write class Foo(Bar), which says "Make a class Foo that inherits from Bar."
When you do this, the language makes any action that you do on instance of Foo also work as if they were done to an instance of Bar.
Doing this lets you put common functionality in the Bar class, then specialize that functionality in the Foo class as needed.

1. Actions on the child imply an action on the parent.
2. Actions on the child override the action on the parent.
3. Actions on the child alter the action on the parent.
'''
# Implicit Inheritance
# when you define a function in the parent, but not in the child.
# very handy for repetitive code you need in many classes.
class Parent(object):

    def implicit(self):
        print "Parent implicit()"

class Child(Parent):

    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# Override Inheritance
class Parent(object):

    def override(self):
        print "Parent override()"

class Child(Parent):

    def override(self):
        print "Child override()"

dad = Parent()
son = Child()

dad.override()
son.override()

# Alter ?
# a special case of overriding where you want to alter the behavior before or after the parent class's version runs.
# use a Pyton build-in function named super to get the Parent version to call <-------- what does this mean?????

class Parent(object):

    def altered(self):
        print "Parent altered()"

class Child(Parent):

    def altered(self):
        print "Child before Parent altered()"
        super(Child, self).altered() #<-- look up what the function is look like in parent
        print "Child after Parent altered()"

dad = Parent()
son = Child()

#dad.altered()
son.altered() # why there's another Parent altered() printed in between??? wrap around the method you try to call.






# ++++++++++++++++ the reason for super() ++++++++++++++++++ #
'''
Multiple Inheritance is when you define a class that inherits from one or more classes, like this:
class SuperFun(Child, BadStuff):
    pass
'''
# using super() with __init__:
# the only place where you need to do some things in a child, then complete the initialization in the parent.
# what is that mean????

class Child(Parent):

    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__() # use super() as a query, to look up if the function is in the base class.

# setting some variables in the __init__ before having the Parent initialize with its Parent.__init__()


# ++++++++++++++++ calling functions in a module +++++++++++++++ #
class Other(object):

    def override(self):
        print "Other override()"

    def implicit(self):
        print "Other implicit()"

    def altered(self):
        print "Other altered()"

class Child(object):

    def __init__(self):
        self.other = Other()
# so here just initialize by importing the functions from class Other()? has-a relationship.

    def implicit(self):
        self.other.implicit()

# call function in other class and define as a function here?
# this is a 'has-a' relationship so I can call the functions from Others!

    def override(self):
        print "Child override()"

    def altered(self):
        print "Child, before Other altered()"
        self.other.altered()
        print "Child, after Other altered()"

son = Child()

son.implicit()
son.override()
son.altered()

'''
When to use "Inheritance" or "Composition"?
This comes down to an attempt to solve the problem of reusable code.
You don't want to have duplicated code all over your software, since that's not clean and efficient.

++++++++++++++++++++++
Inheritance solves this problem by creating a mechanism for you to have implied features in base classes.

Composition solves this by giving you modules and the ability to call functions in other classes.



'''
