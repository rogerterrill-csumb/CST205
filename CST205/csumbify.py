def get_pic():
  return makePicture(pickAFile())
  
def betterBnW(pic):
  pixels = getPixels(pic)
  for p in pixels:
    avg_color = avg_color = (getRed(p)*.299 + getGreen(p)*.587 + getBlue(p)*.114)
    newColor = makeColor(avg_color,avg_color,avg_color)
    setColor(p, newColor)
  return pic
  
def sepia(pic):
  pic = betterBnW(pic)
  width = getWidth(pic)
  height = getHeight(pic)
  for x in range(0, width):
    for y in range(0, height):
      px = getPixel(pic, x, y)
      red = getRed(px)
      green = getGreen(px)
      blue = getBlue(px)
      if( red < 63):
        new_red = red * 1.1
        if new_red > 255:
          new_red = 255
        setRed(px, new_red)
        setBlue(px, blue * 0.9)
      elif( red > 62 and red < 192):
        new_red = red * 1.15
        if new_red > 255:
          new_red = 255
        setRed(px, red * 1.15)
        setBlue(px, blue * 0.85)
      elif( red > 191):
        new_red = red * 1.08
        if new_red > 255:
          new_red = 255
        setRed(px, red * 1.08)
        setBlue(px, blue * 0.93)
  show(pic)
  return pic
  
def replace_pixels(pic, logo, x_target, y_target):
  pic_width = getWidth(pic)
  pic_height = getHeight(pic)
  logo_width = getWidth(logo)
  logo_height = getHeight(logo)
  otter_blue = makeColor(1, 54, 104)
  sepia_pic = sepia(pic)
  
  
  for x in range(0, logo_width,2):
    for y in range(0, logo_height,2):
      px_pic = getPixel(sepia_pic, x + x_target, y + y_target)
      pic_color = getColor(px_pic)
      px_logo = getPixel(logo, x, y)
      logo_color = getColor(px_logo)
      if(distance(logo_color, white) < 65):
        pass
      else:
        setColor(px_pic, otter_blue)
  return pic
  
def add_frame(pic, width, height):
  otter_blue = makeColor(1, 54, 104)
  for x in range(0, width):
    for y in range(0, height):
      if (x == 0)and (y%25 == 0):
        addOvalFilled(pic, x, y, 20, 20, otter_blue)
      elif (y == 0) and (x%25 ==0):
        addOvalFilled(pic, x, y, 20, 20, otter_blue)
      elif (x == width-1) and (y%25 == 0):
        addOvalFilled(pic, x-19, y, 20, 20, otter_blue)
      elif (y == height-1) and (x%25 == 0):
        addOvalFilled(pic, x, y-19, 20, 20, otter_blue)
  return pic
  

def csumbify():
  pic = get_pic()
  logo = get_pic()
  pic_width = getWidth(pic)
  pic_height = getHeight(pic)
  logo_width = getWidth(logo)
  logo_height = getHeight(logo)
  
  x_start = 0;
  y_start = 0;
  
  # Picture is bigger than logo
  if(pic_width > logo_width):
    x_start = (pic_width - logo_width)/2
  if(pic_height > logo_height):
    y_start = (pic_height - logo_height)/2
  if((pic_width < logo_width) or (pic_height < logo_height)):
    print "Picture is too small, must be minimum 500 wide and 283 tall"
    return
     
  pic_converted = replace_pixels(pic, logo, x_start, y_start)
  pic_framed = add_frame(pic_converted, pic_width, pic_height)
  show(pic_framed)
   
    
  
  
