def get_pic():
  return makePicture(pickAFile())

# Problem 1
def vertical_mirror():
  pic = get_pic()
  width = getWidth(pic)
  height = getHeight(pic)
  print width, height
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
  repaint(pic)
  writePictureTo(pic, "C://Users//roger.terrill//Documents//CST205//Photos/vertical_mirror.jpeg")
  
def horizontal_mirror_top_bottom():
  pic = get_pic()
  width = getWidth(pic)
  height = getHeight(pic)
  print width, height
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
  repaint(pic)
  writePictureTo(pic, "C://Users//roger.terrill//Documents//CST205//Photos/horizontal_mirror_top_bottom.jpeg")
  
def horizontal_mirror_bottom_top():
  pic = get_pic()
  width = getWidth(pic)
  height = getHeight(pic)
  print width, height
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
  repaint(pic)
  writePictureTo(pic, "C://Users//roger.terrill//Documents//CST205//Photos/horizontal_mirror_bottom_top.jpeg")
  
def combo_mirror():
  pic = get_pic()
  width = getWidth(pic)
  height = getHeight(pic)
  print width, height
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
  repaint(pic)
  writePictureTo(pic, "C://Users//roger.terrill//Documents//CST205//Photos/combo_mirror.jpeg")
  