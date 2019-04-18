__author__ = "Roger Terrill, Abby Packham, Carlos Orduna"
__copyright__ = "Copyright 2019, CST205"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "rchicasterrill@csumb.edu, apackham@csumb.edu, cordunacorrales@csumb.edu  "
__status__ = "Production"

import random


class Die:
    def __init__(self, value):
        self.value = value

    def roll(self):
        self.value = random.randint(1, 6)
        return self.value


def add_dice(first_die, second_die):
    return first_die + second_die


def craps():
    print("Welcome to Craps")
    point_val = 0
    first_roll = True
    die_1 = Die(0)
    die_2 = Die(0)

    while True:
        requestString("Press [enter] to roll")
        die_1.roll()
        die_2.roll()
        total = add_dice(die_1.value, die_2.value)
        print 'You rolled a ', die_1.value
        print 'And you rolled a ', die_2.value
        print 'For a total ', total
        if first_roll:
            if total == 7 or total == 11:
                print "You win!"
                return
            elif total == 2 or total == 3 or total == 12:
                print "You lose :("
                return
            else:
                print 'Point is ', total 
                point_val = total
                first_roll = False
        else:
            if total == 7:
                print "You lose :(" 
                return
            if total == point_val:
                print "You win :)"
                return