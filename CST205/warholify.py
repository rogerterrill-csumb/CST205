import copy

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
    pic_list = []
    
    for i in range(4):
      pic_list.append(copy.copy(pic))
    
    pic_width = getWidth(pic)
    pic_height = getHeight(pic)
    
    
    target = makeEmptyPicture(pic_width*2, pic_height*2)
    
    pixels = getPixels(pic_list[0])
    for p in pixels:
        r = getRed(p)
        setRed(p, r * 50)
    pyCopy(pic_list[0], target, 0,0)

    pixels = getPixels(pic_list[1])
    for p in pixels:
        r = getGreen(p)
        setGreen(p, r * 30)
    pyCopy(pic_list[1], target, pic_width-1,0)
 
    pixels = getPixels(pic_list[2])
    for p in pixels:
        r = getBlue(p)
        setBlue(p, r * 50)
    pyCopy(pic_list[2], target, 0, pic_height-1)

    
    pixels = getPixels(pic_list[3])
    for p in pixels:
        r = getGreen(p)
        setGreen(p, r - 100)
    pyCopy(pic_list[3], target, pic_width-1,pic_height-1)
    
    
    show(target)
