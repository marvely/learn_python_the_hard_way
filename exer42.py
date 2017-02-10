# understand the difference between a class and an object
# well, they are same thing at different points in time.

# only need to worry about it when you make new classes, or when you use a class.

# "is-a", about objects and classes being related to each other by a class relationship.
#"has-a", about objects and classes that are related only becasue they reference each other.

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a object of Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name attribute
        self.name = name

## Cat is-a object of Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name attribute
        self.name = name

## Person is-a object of a class
class Person(object): #<------ should always do this step on the very bottom part of the class!!!!!!!!!!
# base class~~~~~~~~

    def __init__(self, name):
        ## person has-a name attribute
        self.name = name
        ## person has-a pet of some kind
        self.pet = None # this makes sure that the self.pet attribute of that class is set to a default of None.

## Employee is-a object of a person class
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)

        ## Employee has-a attribute called salary
        self.salary = salary

## Fish is-a object of class object
class Fish(object):
    pass

## Salmon is-a object of Fish
class Salmon(Fish): #<--- inheric from that object, which is a class???
    pass

## Halibut is-a object of Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog('Rover')

## Satan is-a Cat
satan = Cat('Satan')

## mary is-a person
mary = Person('Mary')


## Mary has-a pet which is Satan
mary.pet = satan

print mary
print mary.pet.name
## Frank is-a Employee
frank = Employee('Frank', 120000)

## Frank has-a pet which is Rover
frank.pet = rover

print frank
print frank.pet.name
## Flipper is-a object of class Fish
flipper = Fish()

## crouse is-a object of a class Salmon
crouse = Salmon()

## harry is-a object of class halibut, which is-a object of class fish
harry = Halibut()
'''
Do you think there's such thing as an "is-many" relationship? Read about "multiple inheritance," then avoid it if you can.
'''
### :D
