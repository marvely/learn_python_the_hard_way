# top down
'''
1. Write or draw about the problem
2. Extract key concepts from step1 and research them
3. Create a class hierarchy and object map for the concepts
4. Code the classes and a test to run them
5. Repeat and refine

class Scene(object):

    def enter(self):
        pass

class Engine(object):
    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Death(Scene):

    def enter(self):
        pass

class Central_Corridor(Scene):

    def enter(self):
        pass

class Laser_Weapon_Armory(Scene):

    def enter(self):
        pass

class Bridge(Scene):

    def enter(self):
        pass

class Escape_Pod(Scene):

    def enter(self):
        pass

class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('central_corridor')

a_game = Engine(a_map)

a_game.play()

# bottom up
'''
# +++++++++++++++++ Zed's version of game +++++++++++++++++ #
from sys import exit

from random import randint


class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene("finished")
        print last_scene

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
# already introduced the map functions here, plan ahead!
        # be sure to print out the last scene
            current_scene.enter()

class Death(Scene):

    quips = [
    "You died.\tYou kinda suck at this.",
    "Your mom would be proud... if she were smarter.",
    "Such a luser.",
    "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips) - 1)]
        exit(1)

class Central_Corridor(Scene):

    def enter(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed \nyour entire crew. You are the last surviving member and your last \nmission is to get the neutron destruct bomb from the Weapons Armory, \nput it in the bridge, and blow the ship up after getting into an \nescape pod.\nYou're running down the central corridor to the Weapons Armory when \na Cothon jumps out, red scaly skin, dark grimy teeth, and evil clawn costume \nflowing around his hate filled body. He's blocking the door to the Armory \nand about to pull a weapon to blast you."

        action = raw_input("> ")

        if action == "shoot!":
            print "Quick on the draw you yank out your blaster and fire it at the Gothon. \nHis clawn costume is flowing and moving around his body, which throws \noff your aim. Your lazer hits his costume but misses him entirely. This \ncompletely ruins his brand new costume his mother bought him, which \nmakes him fly into an insane rage and blast you repeatedly in the face until \nyou are dead. Then he eats you."

            return "death"

        elif action == "dodge!":
            print "Like a world class boxer you dodge, weave, slip and slide right \nas the Gothon's blaster cranks a laser past your head. \nIn the middle of your artful dodge your foot slips and you \nbang your head on the metal wall and pass out. \nYou wake up shortly after only to die as the Gothon stomps on \nyour head and eats you."

            return "death"

        elif action == "tell a joke":
            print "Lucky for you they made you learn Gothon insults in the academy. \nYou tell the one gothon joke you know: \nLbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr. \nThe Gothon stops, tries not to laugh, then busts out laughing and can't move. \nWhile he's lauphing you run up and shoot him square in the head, \nputting him down, then jump through the Weapon Armory door."

            return "laser_weapon_armory"

        else:
            print "Does not compute!"
            return "central_corridor"
# doing the scenes before the map object because i need to reference them later.

class Laser_Weapon_Armory(Scene):

    def enter(self):
        print "You do a dive roll into the Weapon Armory, crouch and scan the room \nfor more Gothons that might be hiding. It's dead quiet, too quiet. \nYou stand up and run to the far side of the room and find the \nneutron bomb in its container. There's a keypad lock on the box \nand you need the code to get the bomb out. If you get the code \nwrong 10 times then the lock closes forever and you can't \nget the bomb. the code is 1 digit."

        code = "%d" % randint(1, 9)
        guess = raw_input("[keypad]> ")
        guesses = 1

        while guess != code and guesses < 10:
            print "BZZZZZZZZEEEEEEDDDDDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "The container clicks open and the seal breaks, letting gas out. \nYou grab the neutron bomb and run as fast as you can to the \nbridge where you must place it in the right spot."
            
            return "the_bridge"
# something is wrong... why i get 0 time right, but it return to the guess scene?????

        else:
            print "The lock buzzes one last time and the you hear a sickening \nmelting sound as the mechanism is fused together. \nYou decide to sit there, and finally the Gothons blow up the \nship from their ship and you die."

            return "death"
# cannot exit this loop????

class The_Bridge(Scene):

    def enter(self):
        print "You burst onto the Bridge with the neutron destruct bomb \nunder your aim and surprise 5 Gothons who are trying to \ntake control of the ship. Each of them has an even uglier \nclown costume than the last. They haven't pulled their \nweapons out yet, as they see the active bomb under your \narm and don't want to set it off."

        action = raw_input("> ")

        if action == "throw the bomb":
            print "In a panic you throw the bomb at the group of Gothons \n and make a leap for the door. Right as you drop it a \Gothon shoots you right in the back killing you. \nAs you die you see another gothon frantically try to disarm \nthe bomb. You die knowing they will probably blow up when \nit goes off."
            return "death"

        elif action == "slowly place the bomb":
            print "You point your blaster at the bomb under your arm \nand the Gothons put their hands up and start to sweat. \nYou inch backward to the door, open it, and then carefully \nplace the bomb on the floor, pointing your blaster at it. \nYou then jump back through the door, punch the close botton \n and blast the lock so the Gothons can't get out. \nNow that the bomb is placed you run to the escape pod to \nget off this tin can."
            return "escape_pod"

        else:
            print "Does not compute!"
            return "the_bridge"

class Escape_Pod(Scene):
    def enter(self):
        print "You rush through the ship desperately trying to make it to \nthe escape pod before the whole ship explodes. it seems like \nhardly any Gothons are on the ship, so your run is clear of \ninterference. You get to the chamber with the escape pods, and \nnow need to pick one to take. Some of them could be damaged \nbut you don't have time to look. There's 5 pods, which one \ndo you take?"

        good_pod = randint(1, 5)
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod escapes out into the void of space, then \nimplodes as the hull ruptures, crushing your body \ninto jam jelly."

            return "death"

        else:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod easily slides out into space heading to \nthe planet below. As it flies to the planet, you look \nback and see your ship implode then explode like a \nbright star, taking out the Gothon ship at the same \ntime. You won!"

            return "finished"

class Finished(Scene):

    def enter(self):
        print "You won! Good job."
        return "finished"

# ++++++++++++++++++ need to build this incrementally!!! +++++++++ #
class Map(object):

    scenes = {
        'central_corridor': Central_Corridor(),
        'laser_weapon_armory': Laser_Weapon_Armory(),
        'the_bridge': The_Bridge(),
        'escape_pod': Escape_Pod(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
