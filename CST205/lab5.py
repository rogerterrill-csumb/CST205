def get_pic():
  return makePicture(pickAFile())
  
# Previous Functions
def simpleCopy(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  mypic = makeEmptyPicture(width, height)
  for x in range (0, getWidth(mypic)):
    for y in range (0, getHeight(mypic)):
      p = getPixel(pic, x, y)
      red = getRed(p)
      green = getGreen(p)
      blue = getBlue(p)
      new_pic = getPixel(mypic, x, y)
      setRed(new_pic, red)
      setGreen(new_pic, green)
      setBlue(new_pic, blue)
  show(mypic)
  writePictureTo(mypic, "C://Users//roger.terrill//Documents//CST205//Photos/simple_copy.jpeg")
  return mypic
  
  
# Problem 3
def rotatePic():
  pic = get_pic()
  width = getWidth(pic)
  height = getHeight(pic)
  mypic = makeEmptyPicture(height, width)
  for x in range (0, width):
    for y in range (0, height):
      p = getPixel(pic, x, y)
      red = getRed(p)
      green = getGreen(p)
      blue = getBlue(p)
      new_pic = getPixel(mypic, y , width-x-1)
      setRed(new_pic, red)
      setGreen(new_pic, green)
      setBlue(new_pic, blue)
  show(mypic)
  writePictureTo(mypic, "C://Users//roger.terrill//Documents//CST205//Photos/rotate_pic.jpeg")
  return mypic
  
  
# Problem 4
def shrink():
  pic = get_pic()
  width = getWidth(pic)
  height = getHeight(pic)
  mypic = makeEmptyPicture(width/2, height/2)
  for x in range (0, width, 2):
    for y in range (0, height, 2):
      p = getPixel(pic, x, y)
      red = getRed(p)
      green = getGreen(p)
      blue = getBlue(p)
      new_pic = getPixel(mypic, x/2, y/2)
      setRed(new_pic, red)
      setGreen(new_pic, green)
      setBlue(new_pic, blue)
  show(mypic)
  writePictureTo(mypic, "C://Users//roger.terrill//Documents//CST205//Photos/shrink.jpeg")
  return mypic

# Warm up
def copy_with_border():
  pic = get_pic()
  width = getWidth(pic)
  height = getHeight(pic)
  mypic = makeEmptyPicture(width+200, height+200)
  print mypic
  for x in range (0, width):
    for y in range (0, height):
      p = getPixel(pic, x, y)
      red = getRed(p)
      green = getGreen(p)
      blue = getBlue(p)
      new_pic = getPixel(mypic, x+100, y+100)
      setRed(new_pic, red)
      setGreen(new_pic, green)
      setBlue(new_pic, blue)
  show(mypic)
  writePictureTo(mypic, "C://Users//roger.terrill//Documents//CST205//Photos/copy_with_border.jpeg")
  return mypic
  
# Problem #1
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
  show(target)
  writePictureTo(target, "C://Users//roger.terrill//Documents//CST205//Photos/pyCopy.jpeg")
  return target
  
# Problem #2
def makeCollage():
  pic_list = []
  for i in range(8):
    pic_list.append(get_pic())
  
  #width = getWidth(source)
  #height = getHeight(source)
  #for x in range (0, width):
  #  for y in range (0, height):
  #    p = getPixel(source, x, y)
   #   red = getRed(p)
    #  green = getGreen(p)
     # blue = getBlue(p)
      #new_pic = getPixel(target, x+targetX, y+targetY)
      #setRed(new_pic, red)
      #setGreen(new_pic, green)
      #setBlue(new_pic, blue)
  #show(target)
  #writePictureTo(target, "C://Users//roger.terrill//Documents//CST205//Photos/pyCopy.jpeg")
