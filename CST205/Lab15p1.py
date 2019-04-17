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
    point = 0
    die_1 = Die(0)
    die_2 = Die(0)
    die_1.roll()
    die_2.roll()

    total = add_dice(die_1.value, die_2.value)

    if total == 7 or total == 11:
        print("You win!")
        return
    elif total == 2 or total == 3 or total == 12:
        print("You lose :(")
    else:
        point = total


if __name__ == '__main__':
    craps()
