__author__ = "Roger Terrill, Abby Packham, Carlos Orduna"
__copyright__ = "Copyright 2019, CST205"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "rchicasterrill@csumb.edu, apackham@csumb.edu, cordunacorrales@csumb.edu  "
__status__ = "Production"


# Type quest() to begin your adventure
# Displays the welcome screen
def welcome():
  printNow("---------------Welcome to team 4's Adventure!---------------")
  printNow("You find yourself waking up in the aftermath of an explosion, you are a wizard in this land")
  printNow("Depending on where you are, you'll be able to go north, south, east or west by typing that direction")
  printNow("Type help to display this help menu")
  printNow("Type exit to quit at any time")

# Displays the help menu
def help():
  printNow("---------------Help Menu--------------")
  printNow("Depending on where you are, You'll be able to go north, south, east or west by typing that direction")
  printNow("Type help to redisplay this introduction")
  printNow("Type exit to quit at any time")

# Traveling directions
def direction():
  return (requestString("What direction do you move?").lower())

# Search the tavern's rubble
def selection():
  return (requestString("Search or return East?").lower())

# Display introduction to the game                
def Introduction():
  printNow("---------------Crossroads--------------")
  printNow("Your robe is in tatters and burnt. You find yourself in one piece with minor bruises, cuts and a light headache. You are laying on snow and mud")
  printNow("The tavern you were spending the night in got seized and an explosion destroyed the building")
  printNow("Only the debris from the walls that once supported the lively atmosphere remain around you. Not a body in sight")  
  printNow("You stand and regain your balance")
  printNow("-The path [North] has tiny footprints on the snow, alongise a wide track")
  printNow("-The path [East] has tiny footprints on the snow comming from this road")
  printNow("-The path [South] goes downhill to a river below")
  printNow("-To the [West] you see most of the rubble left from the building")
  return (direction())

# Display what is at the crossroads section, start of the game
def crossroads():
  printNow("---------------Crossroads--------------")
  printNow("You find yourself in the middle of the crossroads, where a tavern once stood")
  printNow("-The path [North] has tiny footprints next to a wide track on the snow going down this road")
  printNow("-The path [East] has tiny footprints on the snow comming from this road")
  printNow("-The path [South] goes downhill to a river below")
  printNow("-To the [West] you see most of the rubble left from the building")
  return (direction())

# Directions once you reach the North Path
def followFootprints():
  printNow("---------------North Path--------------")
  printNow("You see a tiny purple creature dragging and bashing a chest with a familar crest, it resembles that of the tavern's")
  printNow("-Continue [North] and approach the purple creature")
  printNow("-Return [South] to the crossroads")
  return(direction())

# Game over because the player was no prepared.
def confrontImp():
  printNow("---------------Strange Creature--------------")
  printNow("You recognize the creature as a mischievous demonic imp, but continue towards it")
  printNow("The imp loses interest on the chest once it notices you and, with a shriek, jumps towards you bearing its fangs")
  printNow("Unfortunately you didn't have any of your gear and the Imp finishes you off")
  return("exit")
  
# Game won, you killed the imp.
def defeatImp():
  printNow("---------------Defeated the Imp--------------")
  printNow("You recognize the creature as a mischievous demonic imp, but continue towards it")
  printNow("The imp loses interest on the chest once it notices you and, with a shriek, jumps towards you bearing its fangs")
  printNow("Fortunately you have the weapon and you finish the Imp off")
  printNow("Congratulations! YOU HAVE MADE IT TO THE BAR SAFELY!!! Have a drink!")
  return("exit")

# At east path, display where you can go to next
def retraceFootprints():
  printNow("---------------East Path--------------")
  printNow("You decide to retrace the origin of the footprints and walk East")
  printNow("The older footprints are begining to get covered by snow and you are starting to lose the track of where they started from")
  printNow("You come accross a rope bridge that has seen better days")
  printNow("Below is a river, you think to yourself that it would be wise not to attempt to cross")
  printNow("-Continue [East] and cross the rope bridge")
  printNow("-Return [West] towards the crossroads")
  return(direction())

# We recieve a key by crossing the bridge
def ropeBridge():
  printNow("---------------Bridge--------------")
  printNow("You go against your better judgement and decide to attempt to cross the bridge")
  printNow("After a few steps one of the many wood plataforms breaks underneath your feet and you fall a few meters towards the river below")
  printNow("The fall leaves you a bit hurt but the river is deep enough that no rocks were on your landing")
  printNow("You find yourself at the river bank south from the crossroads")
  printNow("Probably could use a rope and bow and arrow to cross it")

# Provided with choices on where to head to next
def riverBank():
  printNow("---------------River Bank--------------")
  printNow("You wash your face off at the river bank")
  printNow("The moon shines bright above the sky, illuminating your night and providing some comfort")
  printNow("You sit on a stone by the river and decide to take a short break")
  printNow("The only path from here is back up to the crossroads")
  printNow("Maybe ... rest")
  printNow("-Go [North] back to the Crossroads")
  printNow("-Remain [South]")
  return (direction()) 

# Choices on how to examine the rubble
def examineRubble(search):
  printNow("---------------Tavern's Debris--------------")
  printNow("You search through the rubble but don't find any of your possessions in the dark")
  printNow("-you can '[Search]'")
  printNow("-Return [East] to the crossroads")
  while selection() == 'search':
    search += 1
    if search == 2:
      printNow("You found ROPE!, maybe if you keep searching you'll find the bow and arrow")
    elif search == 4:
      printNow("You found a Bow and Arrow!, lets go cross that bridge")
      break

  return(selection())
  
# Provided with choices on where to head to next
def cave():
  printNow("---------------Cave--------------")
  printNow("You have made it to the cave")
  printNow("You see something shinning faintly and approach it")
  printNow("It's the BLADES OF CHAOS")
  printNow("Now you are prepared for your journey")
  printNow("-Go [West] back to the Bridge")
  return (direction(), true) 

def secret_room():
  printNow("---------------Cave--------------")
  printNow("While resting, the floor underneath you openned")
  printNow("You fall into a cave")
  printNow("In the corner you see an bright light")
  printNow("You pick up the Leviathan AXE")
  printNow("-Go [North] back to the River")
  return (direction(), true)
  
  
#Legend for counter
#count 0 = Quest start
#count 1 = Crossroads (Start)
#count 2 = North towards Imp
#count 3 = East towards bridge
#count 4 = South towards river
#count 5 = West towards Rubble
#count 6 = Approach the Imp
#count 7 = Attempt to cross bridge
#count 8 = Go into cave
#count 9 = Secret Chamber with weapon

# Function that begins the game
def quest():
  welcome()
  key = "start"
  counter = 0
  weapon = false
  search = 0
  #Start
  while (key != 'exit'):
    if key == "help":
      help()
      key = "key"
    #Introduction
    elif counter == 0:
      counter = 1
      key = Introduction()
      if key == "north":
        counter = 2
      elif key == "east":
        counter = 3
      elif key == "south":
        counter = 4
      elif key == "west":
        counter = 5
    #Every time you return to the main road
    elif counter == 1:
      key = crossroads()
      if key == "north":
        counter = 2
      elif key == "east":
        counter = 3
      elif key == "south":
        counter = 4
      elif key == "west":
        counter = 5
    #If you go north from the main road
    elif counter == 2:
      key = followFootprints()
      if key == "north":
        counter = 6
      elif key == "south":
        counter = 1
    #if you go east from the main road
    elif counter == 3:
      key = retraceFootprints()
      if key == "east" and search > 3:
        counter = 8
      elif key == "east" and search < 4:
          counter = 7
      elif key == "west":
        counter = 1
    #if you go south from the main road
    elif counter == 4:
      key = riverBank()
      if key == "north":
        counter = 1
      elif key == "south":
        printNow("You remain in this area, maybe ... rest")
        counter = 4
      elif key == "rest":
        counter = 9
    #if you go west towards the rubble
    elif counter == 5:
      key = examineRubble(search)
      if key == "search":
        printNow("You continue searching the rubble")
        counter = 5
      if key == "east":
        counter = 1
    #if you go north towards imp
    elif counter == 6:
      if weapon == true:
        key = defeatImp()
      else:  
        key = confrontImp()
    #if you attempt to cross the bridge
    elif counter == 7:
      ropeBridge()
      counter = 4
    elif counter == 8:
      key, weapon = cave()
      if key == "west":
        counter = 3
    elif counter == 9:
      key, weapon = secret_room()
      if key == "north":
        counter = 4
  printNow("Your adventure has ended.")