""" Provides list of functions to create a St. Patrick's Day Card
"""

__author__ = "Roger Terrill, Abby Packham, Carlos Orduna"
__copyright__ = "Copyright 2019, CST205"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "rchicasterrill@csumb.edu, apackham@csumb.edu, cordunacorrales@csumb.edu  "
__status__ = "Production"


def get_pic():
  return makePicture(pickAFile())
  
  
# Warmup
def draw():
  pic = get_pic()
  addOvalFilled(pic, 500, 500, 100, 100, white)
  addOvalFilled(pic, 512, 425, 75, 75, white)
  addOvalFilled(pic, 525, 375, 50, 50, white)
  show(pic)
  
# Problem 1
def mirror(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  mirror = makeEmptyPicture(width, height)
  for x in range(0, width):
    for y in range(0, height):
      p = getPixel(pic, x, y)
      red = getRed(p)
      green = getGreen(p)
      blue = getBlue(p)
      mp = getPixel(mirror, width-x-1, y)
      setRed(mp, red)
      setGreen(mp, green)
      setBlue(mp, blue)
  return mirror

def chromakey(green_pic, background_pic):
  background_green = makeColor(61,255,15)
  width = getWidth(green_pic)
  height = getHeight(green_pic)
  for x in range(0, width):
    for y in range(0, height):
      px = getPixel(green_pic, x, y)
      color = getColor(px)
      background_px = getPixel(background_pic, x, y)
      background_color = getColor(background_px)
      if distance(color, background_green) < 80.0:
        setColor(px, background_color)
  return green_pic 
  
def card():
  green_screen = get_pic()
  background = get_pic()
  logo = get_pic()
  header1 = "Happy St."
  header2 = "Patrick's Day..."
  footer = "...From Space"
  paddy_green = makeColor(0, 102, 0) 
  chromakey(green_screen, background)
  import java.awt.Font as Font
  myFont = makeStyle("Comic Sans", Font.BOLD, 80)
  addTextWithStyle(green_screen, 229, 104, header1, myFont, black)
  addTextWithStyle(green_screen, 225, 100, header1, myFont, white)
  addTextWithStyle(green_screen, 140, 200, header2, myFont, white)
  addTextWithStyle(green_screen, 136, 196, header2, myFont, paddy_green)
  addTextWithStyle(green_screen, 140, 900, footer, myFont, black)
  addTextWithStyle(green_screen, 144, 904, footer, myFont, white)
  pyCopy(logo, green_screen, 50, 240)
  mirror_logo = mirror(logo)
  pyCopy(mirror_logo, green_screen, 470, 240)
  show(green_screen)
  writePictureTo(green_screen, "C://Developing//School//CST205//card.jpeg")
  