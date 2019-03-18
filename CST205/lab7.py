def get_pic():
  return makePicture(pickAFile())
  
  
# Warmup
def draw():
  pic = get_pic()
  addOvalFilled(pic, 500, 500, 100, 100, white)
  addOvalFilled(pic, 512, 425, 75, 75, white)
  addOvalFilled(pic, 525, 375, 50, 50, white)
  show(pic)