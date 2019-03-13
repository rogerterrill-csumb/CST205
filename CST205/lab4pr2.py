# Problem 2
def simplePic():
  mypic = makeEmptyPicture(100, 100)
  for x in range (0, getWidth(mypic)):
    for y in range (0, getHeight(mypic)):
      setColor(getPixel(mypic, x, y), blue)
  show(mypic)
  return mypic