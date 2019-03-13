def get_pic():
  return makePicture(pickAFile())

# Problem 2
def simplePic():
  mypic = makeEmptyPicture(100, 100)
  for x in range (0, getWidth(mypic)):
    for y in range (0, getHeight(mypic)):
      setColor(getPixel(mypic, x, y), blue)
  show(mypic)
  return mypic
  
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
  writePictureTo(pic, "C://Users//roger.terrill//Documents//CST205//Photos/simple_copy.jpeg")
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
  writePictureTo(pic, "C://Users//roger.terrill//Documents//CST205//Photos/rotate_pic.jpeg")
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
  writePictureTo(pic, "C://Users//roger.terrill//Documents//CST205//Photos/shrink.jpeg")
  return mypic
  
  
    
    
  