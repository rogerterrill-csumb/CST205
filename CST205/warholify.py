def get_pic():
    file = pickAFile()
    pic = makePicture(file)
    return pic
    
def pyCopy(source, target, targetX, targetY):
  width = getWidth(source)
  height = getHeight(source)
  for x in range (0, width):
    for y in range (0, height):
      p = getPixel(source, x, y)
      red = getRed(p)
      green = getGreen(p)
      blue = getBlue(p)
      new_pic = getPixel(target, x+targetX, y+targetY)
      setRed(new_pic, red)
      setGreen(new_pic, green)
      setBlue(new_pic, blue)    
  return target
 

def warholify():
    pic = get_pic()
    
    pic_width = getWidth(pic)
    pic_height = getHeight(pic)
    
    red = pic
    green = pic
    blue = pic
    pink = pic
    
    target = makeEmptyPicture(pic_width*2, pic_height*2)
    pixels = getPixels(red)
    for p in pixels:
        r = getRed(p)
        setRed(p, r * 50)
    pyCopy(red, target, 0,0)

    
    pixels = getPixels(green)
    for p in pixels:
        r = getGreen(p)
        setGreen(p, r * 30)
    pyCopy(green, target, pic_width-1,0)
 
    pixels = getPixels(blue)
    for p in pixels:
        r = getBlue(p)
        setBlue(p, r * 50)
    pyCopy(blue, target, 0, pic_height-1)

    
    pixels = getPixels(pink)
    for p in pixels:
        r = getGreen(p)
        setGreen(p, r - 100)
    pyCopy(blue, target, pic_width-1,pic_height-1)
    
    show(target)
