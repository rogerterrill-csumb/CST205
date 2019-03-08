# Warm up
def get_pic():
  return makePicture(pickAFile())
  
def halfRed():
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    setRed(p, r*0.5)
  repaint(pic)
  
#Problem 1
def lessRed(num):
  percentage = num / 100.0
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    setRed(p, r*percentage)
  repaint(pic)
 
#Problem 2
def moreRed(num):
  percentage = num / 100.0 + 1
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    newRed = r*percentage
    if newRed > 255:
      newRed = 255
    setRed(p, newRed)
  repaint(pic)