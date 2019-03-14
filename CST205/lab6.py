def get_pic():
  return makePicture(pickAFile())


# Previous Functions
def betterBnW(pic):
  pixels = getPixels(pic)
  for p in pixels:
    avg_color = avg_color = (getRed(p)*.299 + getGreen(p)*.587 + getBlue(p)*.114)
    newColor = makeColor(avg_color,avg_color,avg_color)
    setColor(p, newColor)
  return pic


def changeCat1(newColor):
  pic = get_pic()
  for px in getPixels(pic):
    color = getColor(px)
    if distance(color, black) < 50.0:
      setColor(px, newColor)
  show(pic)
  return pic
  
def changeCat2(newColor):
 pic = get_pic()
 ltgray = makeColor(114, 112, 133)
 aqua = makeColor(51, 204, 255)
 for x in range(1, 160):
   for y in range(0, 250):
     px = getPixel(pic, x, y)
     color = getColor(px)
     if distance(color, black) < 50.0:
       setColor(px, newColor)
     if distance(color, ltgray) < 50.0:
       setColor(px, aqua)
 show(pic)
 return pic
 
# Warm Up
def red_eye_correction():
  pic = get_pic()
  red_eye = makeColor(200,32,21)
  natural_black = makeColor(28, 13, 6)
  for x in range(53, 296):
    for y in range(207, 276):
      px = getPixel(pic, x, y)
      color = getColor(px)
      if distance(color, red_eye) < 100.0:
        setColor(px, natural_black)
  show(pic)
  return pic
  
# Problem 1
def sepia():
  pic = get_pic()
  pic = betterBnW(pic)
  width = getWidth(pic)
  height = getHeight(pic)
  for x in range(0, width):
    for y in range(0, height):
      px = getPixel(pic, x, y)
      red = getRed(px)
      green = getGreen(px)
      blue = getBlue(px)
      if( red < 63):
        new_red = red * 1.1
        if new_red > 255:
          new_red = 255
        setRed(px, new_red)
        setBlue(px, blue * 0.9)
      elif( red > 62 and red < 192):
        new_red = red * 1.15
        if new_red > 255:
          new_red = 255
        setRed(px, red * 1.15)
        setBlue(px, blue * 0.85)
      elif( red > 191):
        new_red = red * 1.08
        if new_red > 255:
          new_red = 255
        setRed(px, red * 1.08)
        setBlue(px, blue * 0.93)
  show(pic)
  return pic
  
# Problem 2
def Artify():
  pic = get_pic()
  width = getWidth(pic)
  height = getHeight(pic)
  for x in range(0, width):
    for y in range(0, height):
      px = getPixel(pic, x, y)
      red = getRed(px)
      if( red < 64):
        setRed(px, 31)
      elif( red > 63 and red < 128):
        setRed(px, 95)
      elif( red > 127 and red < 192):
        setRed(px, 159)
      elif( red > 192 and red < 256):
        setRed(px, 223)
        
      green = getGreen(px)
      if( green < 64):
        setGreen(px, 31)
      elif( green > 63 and green < 128):
        setGreen(px, 95)
      elif( green > 127 and green < 192):
        setGreen(px, 159)
      elif( green > 192 and green < 256):
        setGreen(px, 223)
        
      blue = getBlue(px)
      if( blue < 64):
        setBlue(px, 31)
      elif( blue > 63 and blue < 128):
        setBlue(px, 95)
      elif( blue > 127 and blue < 192):
        setBlue(px, 159)
      elif( blue > 192 and blue < 256):
        setBlue(px, 223)

  show(pic)
  return pic
    
    
 
