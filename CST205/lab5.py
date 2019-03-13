def get_pic():
  return makePicture(pickAFile())

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
  writePictureTo(pic, "C://Users//roger.terrill//Documents//CST205//Photos/copy_with_border.jpeg")
  return mypic
  
  