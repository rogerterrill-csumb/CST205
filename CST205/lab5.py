import random
def get_pic():
  return makePicture(pickAFile())

# Previous Functions
def vertical_mirror(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  for x in range(0, width/2):
    for y in range(0, height):
      p = getPixel(pic, x, y)
      red = getRed(p)
      green = getGreen(p)
      blue = getBlue(p)
      mp = getPixel(pic, width-x-1, y)
      setRed(mp, red)
      setGreen(mp, green)
      setBlue(mp, blue)
  print "Vertical Mirror Done!"
  return pic
  
def horizontal_mirror_top_bottom(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  for x in range(0, width):
    for y in range(0, height/2):
      p = getPixel(pic, x, y)
      red = getRed(p)
      green = getGreen(p)
      blue = getBlue(p)
      mp = getPixel(pic, x, height - y - 1)
      setRed(mp, red)
      setGreen(mp, green)
      setBlue(mp, blue)
  print "Horizontal Mirror Top to Bottom Done!"
  return pic
  
def horizontal_mirror_bottom_top(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  for x in range(0, width):
    for y in range(height/2, height):
      p = getPixel(pic, x, y)
      red = getRed(p)
      green = getGreen(p)
      blue = getBlue(p)
      mp = getPixel(pic, x, height - y - 1)
      setRed(mp, red)
      setGreen(mp, green)
      setBlue(mp, blue)
  print "Horizontal Mirror Bottom Top Done!"
  return pic
  
def combo_mirror(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  for x in range(0, width/2):
    for y in range(0, height):
      p = getPixel(pic, x, y)
      red = getRed(p)
      green = getGreen(p)
      blue = getBlue(p)
      mp = getPixel(pic, width-x-1, y)
      setRed(mp, red)
      setGreen(mp, green)
      setBlue(mp, blue)
  for x in range(0, width):
    for y in range(0, height/2):
      p = getPixel(pic, x, y)
      red = getRed(p)
      green = getGreen(p)
      blue = getBlue(p)
      mp = getPixel(pic, x, height - y - 1)
      setRed(mp, red)
      setGreen(mp, green)
      setBlue(mp, blue)
  print "Combo Mirror Done!"
  return pic


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
  return mypic
  
def rotatePic(pic):
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
  print "Rotate Picture Done!"
  return mypic
  
def shrink(pic):
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
  print "Shrink Done!"
  return mypic

# Warm up
def copy_with_border(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  mypic = makeEmptyPicture(width+200, height+200)
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
  print "Copy With Border Done!"
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
  return target
  
# Problem #2
def makeCollage():
  pic_list = []
  for i in range(8):
    pic_list.append(get_pic())
  mypic = makeEmptyPicture(2550, 3300)
  
  vertical_mirror(pic_list[0])
  horizontal_mirror_top_bottom(pic_list[1])
  combo_mirror(pic_list[2])
  pic_list[3] = rotatePic(pic_list[3])
  copy_with_border(pic_list[4])
  pic_list[5] = shrink(pic_list[5])
  combo_mirror(pic_list[6])
  pic_list[7] = shrink(pic_list[7])
  vertical_mirror(pic_list[7])

  for i in range(len(pic_list)):
    x = random.randint(0, 2550 - getWidth(pic_list[i]))
    y = random.randint(0, 3300 - getHeight(pic_list[i]))
    collage = pyCopy(pic_list[i], mypic, x, y)
    print "Picture",i+1, "finished"
  writePictureTo(collage, "C://Developing//School//CST205//makeCollage.jpeg")
