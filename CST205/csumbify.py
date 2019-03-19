def get_pic():
  return makePicture(pickAFile())
  
def replace_pixels(pic, logo, x_target, y_target):
  pic_width = getWidth(pic)
  pic_height = getHeight(pic)
  logo_width = getWidth(logo)
  logo_height = getHeight(logo)
  
  for x in range(0, logo_width):
    for y in range(0, logo_height):
      px_pic = getPixel(pic, x + x_target, y + y_target)
      pic_color = getColor(px_pic)
      px_logo = getPixel(logo, x, y)
      logo_color = getColor(px_logo)
      if(distance(logo_color, white) < 65):
        pass
      else:
        setColor(px_pic, black)
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
  show(pic_converted)
   
    
  
  
