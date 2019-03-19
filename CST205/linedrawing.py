def get_pic():
  return makePicture(pickAFile())
  
def betterBnW():
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    avg_color = avg_color = (getRed(p)*.299 + getGreen(p)*.587 + getBlue(p)*.114)
    newColor = makeColor(avg_color,avg_color,avg_color)
    setColor(p, newColor)
  return pic

  
def line_drawing(tolerance):
  drawing = betterBnW()
  width = getWidth(drawing)
  height = getHeight(drawing)
  for x in range(0, width-1):
   for y in range(0, height-1):
     px = getPixel(drawing, x, y)
     main_pixel = getColor(px)
     
     px_right = getPixel(drawing, x+1, y)
     right_pixel = getColor(px_right)
     
     px_bottom = getPixel(drawing, x, y+1)
     bottom_pixel = getColor(px_bottom)
     
     right_distance = distance(main_pixel, right_pixel)
     bottom_distance = distance(main_pixel, bottom_pixel)
     
     if right_distance < tolerance and bottom_distance < tolerance:
       setColor(px, white)
     else:
       setColor(px, black)
  show(drawing)
  
def line_drawing2(tolerance):
  drawing = betterBnW()
  width = getWidth(drawing)
  height = getHeight(drawing)
  for x in range(0, width-1):
   for y in range(0, height-1):
     px = getPixel(drawing, x, y)
     main_pixel = (getRed(px) + getGreen(px) + getBlue(px))/3
     
     px_right = getPixel(drawing, x+1, y)
     right_pixel = (getRed(px_right) + getGreen(px_right) + getBlue(px_right))/3
     
     px_bottom = getPixel(drawing, x, y+1)
     bottom_pixel = (getRed(px_bottom) + getGreen(px_bottom) + getBlue(px_bottom))/3
     
     right_distance = abs(main_pixel - right_pixel)
     bottom_distance = abs(main_pixel - bottom_pixel)
     
     if right_distance > tolerance and bottom_distance > tolerance:
       setColor(px, black)
     else:
       setColor(px, white)
  show(drawing)