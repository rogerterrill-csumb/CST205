__author__ = "Roger Terrill, Abby Packham, Carlos Orduna"
__copyright__ = "Copyright 2019, CST205"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "rchicasterrill@csumb.edu, apackham@csumb.edu, cordunacorrales@csumb.edu  "
__status__ = "Production"


# Type quest() to begin your adventure
# Displays the welcome screen
def welcome():
  showInformation("------------Welcome to team 4's Adventure!------------\n"
  "You find yourself waking up in the aftermath of an explosion\n\n"
  "Depending on where you are\n" 
  "you'll be able to go north, south, east or west by typing that direction\n\n"
  "Type help to display this help menu\n\n"
  "Type exit to quit at any time")

# Displays the help menu
def help():
  showInformation("------------Help Menu-----------\n"
  "Depending on where you are\n" 
  "you'll be able to go north, south, east or west by typing that direction\n\n"
  "Type help to display this help menu\n\n"
  "Type exit to quit at any time")

# Traveling directions
def direction():
  return (requestString("What direction do you move?").lower())

# Search the tavern's rubble
def selection():
  return (requestString("Search or return East?").lower())

# Display introduction to the game                
def Introduction(name):
  showInformation("---------------Crossroads--------------\n"
  "Your robe is in tatters and burnt. You find yourself in one piece with minor bruises, cuts and a light headache.\n" 
  "You are laying on snow and mud\n\n"
  "The only thing that you remember is your name: " + name + "\n\n"
  "The tavern you were spending the night in got seized and an explosion destroyed the building\n\n"
  "Only the debris from the walls that once supported the lively atmosphere remain around you.\n Not a body in sight\n"  
  "You stand and regain your balance\n")
  printNow("\n------\n\n-The path [North] has tiny footprints on the snow, alongise a wide track\n"
  "-The path [East] has tiny footprints on the snow comming from this road\n"
  "-The path [South] goes downhill to a river below\n"
  "-To the [West] you see most of the rubble left from the building\n")
  return (direction())

# Display what is at the crossroads section, start of the game
def crossroads():
  showInformation("---------------Crossroads--------------\n"
  "You find yourself in the middle of the crossroads, where a tavern once stood\n")
  printNow("\n\n-The path [North] has tiny footprints next to a wide track on the snow going down this road\n"
  "-The path [East] has tiny footprints on the snow comming from this road\n"
  "-The path [South] goes downhill to a river below\n"
  "-To the [West] you see most of the rubble left from the building\n")
  return (direction())

# Directions once you reach the North Path
def followFootprints():
  showInformation("---------------North Path--------------\n"
  "You see a tiny purple creature dragging and bashing a chest with a familar crest, it resembles that of the tavern's")
  printNow("\n\n-Continue [North] and approach the purple creature\n"
  "-Return [South] to the crossroads\n")
  return(direction())

# Game over because the player was no prepared.
def confrontImp():
  showInformation("---------------Strange Creature--------------\n"
  "You recognize the creature as a mischievous demonic imp, but continue towards it\n"
  "The imp loses interest on the chest once it notices you and, with a shriek, jumps towards you bearing its fangs\n"
  "Unfortunately you didn't have any of your gear and the Imp finishes you off\n")
  return("exit")
  
# Game won, you killed the imp.
def defeatImp():
  showInformation("---------------Defeated the Imp--------------\n"
  "You recognize the creature as a mischievous demonic imp, but continue towards it\n"
  "The imp loses interest on the chest once it notices you and, with a shriek, jumps towards you bearing its fangs\n"
  "Fortunately you are armed and you finish off the Imp\n"
  "Congratulations! YOU HAVE MADE IT TO THE BAR SAFELY!!! Have a drink!\n")
  return("exit")

# At east path, display where you can go to next
def retraceFootprints():
  showInformation("---------------East Path--------------\n"
  "You decide to retrace the origin of the footprints and walk East\n"
  "The older footprints are begining to get covered by snow and you are starting to lose the track of where they started from\n"
  "You come accross a rope bridge that has seen better days\n"
  "Below is a river, you think to yourself that it would be wise not to attempt to cross\n")
  printNow("\n\n-Continue [East] and cross the rope bridge\n"
  "-Return [West] towards the crossroads\n")
  return(direction())

# We recieve a key by crossing the bridge
def ropeBridge():
  showInformation("---------------Bridge--------------\n"
  "You go against your better judgement and decide to attempt to cross the bridge\n"
  "After a few steps one of the many wood plataforms breaks underneath your feet and you fall a few meters towards the river below\n"
  "The fall leaves you a bit hurt but the river is deep enough that no rocks were on your landing\n"
  "You find yourself at the river bank south from the crossroads\n"
  "Probably could use a rope and bow and arrow to cross it\n")

# Provided with choices on where to head to next
def riverBank():
  showInformation("---------------River Bank--------------\n"
  "You wash your face off at the river bank\n"
  "The moon shines bright above the sky, illuminating your night and providing some comfort\n"
  "You sit on a stone by the river and decide to take a short break\n"
  "The only path from here is back up to the crossroads\n"
  "Or maybe... rest")
  printNow("\n\n-Go [North] back to the Crossroads\n"
  "-Or remain [South]")
  return (direction()) 

# Choices on how to examine the rubble
def examineRubble():
  showInformation("---------------Tavern's Debris--------------\n"
  "You can search through the rubble or return to the crossroads")
  printNow("\n\n-you can '[Search]'\n"
  "-Return [East] to the crossroads\n") 
  return(selection())
  
# Provided with choices on where to head to next
def cave():
  showInformation("---------------Cave--------------\n"
  "You have made it to the cave\n"
  "You see something shinning faintly and approach it\n"
  "It's the BLADES OF CHAOS\n"
  "Now you are prepared for your journey\n")
  printNow("\n\n-Go [West] back to the Bridge")
  return (direction(), true) 

def secret_room():
  showInformation("---------------Cave--------------\n"
  "While resting, the floor underneath you openned\n"
  "You fall into a cave\n"
  "In the corner you see an bright light\n"
  "You pick up the LEVIATHAN AXE\n")
  printNow("\n\n-Go [North] back to the River\n")
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
  inventory = []
  name = requestString("Please enter your name")
  #Start
  while (key != 'exit'):
    if key == "help":
      help()
      key = "key"
    #Introduction
    elif counter == 0:
      counter = 1
      key = Introduction(name)
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
      if key == "east" and "Bow" in inventory:
        counter = 8
      elif key == "east" and "Bow" not in inventory:
          counter = 7
      elif key == "west":
        counter = 1
    #if you go south from the main road
    elif counter == 4:
      key = riverBank()
      if key == "north":
        counter = 1
      elif key == "south":
        showInformation("\nYou remain in this area, maybe ... rest")
        counter = 4
      elif key == "rest":
        counter = 9
    #if you go west towards the rubble
    elif counter == 5 and "Bow" not in inventory:
      key = examineRubble()
      if key == "search":
        printNow("You found a bow and arrow with some rope, you could use this to cross a gap")
        inventory.append("Bow")
        counter = 5
      if key == "east":
        counter = 1
    elif counter == 5 and "Bow" in inventory:
        printNow("You don't find any other useful things and return to the crossroads. ")
        counter = 1
    #if you go north towards imp
    elif counter == 6:
      if "Axe" and "Blades" in inventory:
        printNow("With the LEVIATHAN AXE and the BLADES OF CHAOS you proceed forward")
        key = defeatImp()
      elif "Axe" in inventory:
        printNow("With the LEVIATHAN AXE you proceed forward")
        key = defeatImp()
      elif "Blades" in inventory:
        printNow("With the BLADES OF CHAOS you proceed forward")
        key = defeatImp()
      else:  
        key = confrontImp()
    #if you attempt to cross the bridge
    elif counter == 7:
      ropeBridge()
      counter = 4
    elif counter == 8:
      if "Blades" not in inventory:  
        inventory.append("Blades")
        key, weapon = cave()
        if key == "west":
          counter = 3
      elif "Blades" in inventory:
        counter = 3
    elif counter == 9:
      if "Axe" not in inventory:
        inventory.append("Axe")
        key, weapon = secret_room()
        if key == "north":
          counter = 4
      elif "Axe" in inventory:
        counter = 4
  showInformation(name +"'s adventure has ended.")