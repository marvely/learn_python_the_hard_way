# ++++++++++++++++ branches and functions ++++++++++++++ #
from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"

    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)

    else:
        dead("man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0) #<----- what does this do???

    else:
        dead("You greedy bastard!")

def bear_room():
    print "There is a bear."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"

    bear_moved = False

    while True:  #<------ that makes an infinite loop.
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt_bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

def dead(why):
    print why, "Good job!"
    exit(0) #<------- the number passed in will indicate an error or not. Here 0 means false, no error, just exit.
    '''
     If you do exit(1) then it will be an error, but exit(0) will be a good exit. The reason it's backward from normal boolean logic (with 0==False) is that you can use different numbers to indicate different error results. You can do exit(100) for a different error result than exit(2) or exit(1).
    '''

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your hand?"
    choice = raw_input("> ")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()  # <---- what is this do within this function?????? looping over this function again.

start()
