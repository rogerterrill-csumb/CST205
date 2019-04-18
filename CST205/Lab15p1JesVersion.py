__author__ = "Roger Terrill, Abby Packham, Carlos Orduna"
__copyright__ = "Copyright 2019, CST205"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "rchicasterrill@csumb.edu, apackham@csumb.edu, cordunacorrales@csumb.edu  "
__status__ = "Production"

import random
import calendar
import datetime


class Die:
    def __init__(self, value):
        self.value = value

    def roll(self):
        self.value = random.randint(1, 6)
        return self.value


def add_dice(first_die, second_die):
    return first_die + second_die

# Craps Game
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
                

def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = this_year - target_date
    return dt.days


def print_birthday_information(days):
    if days < 0:
        print "You had your birthday" + str(-days) + "days ago this year."
    elif days > 0:
        print "Your birthday is in" + str(days) + "days"
    else:
        print("Happy Birthday!!!")              

# Birthday Check                                                                                                
def bday_calendar():
  day = int(requestString("What day number were you born?"))
  month = int(requestString("What month number were you born?"))
  year = int(requestString("What year number were you born? YYYY"))
  bday = datetime.date(year, month, day)
  
  print calendar.month(year, month)
    
  today = datetime.date.today()
  number_of_days = compute_days_between_dates(bday, today)
  print_birthday_information(number_of_days)
  
# Declaration of Independence
def declaration():
  day = 4
  month = 7
  year = 1776
  day_of_week = calendar.weekday(year, month, day)
  day_of_week_name = calendar.day_name[day_of_week]
  month_name = calendar.month_name[month]
  print day_of_week_name + " " + month_name + " " + str(day) + "th " + str(year)
  