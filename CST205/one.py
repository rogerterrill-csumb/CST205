#!/usr/bin/env python
""" Provides list of functions to manipulate images
"""

__author__ = "Abby Packham, Carlos Orduna, Roger Terrill"
__copyright__ = "Copyright 2019, CST205"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "apackham@csumb.edu, cordunacorrales@csumb.edu, rchicasterrill@csumb.edu "
__status__ = "Production"


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
  
#Problem 3
def roseColoredGlasses():
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    b = getBlue(p)
    g = getGreen(p)
    setRed(p, r + 50)
    setBlue(p, b - 50)
    setGreen(p, g - 50) 
  repaint(pic)
  
#Problem 4
def lightenUp():
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    newColor = makeColor(getRed(p)+50, getGreen(p)+50, getBlue(p)+50)
    setColor(p, newColor)
  repaint(pic)
    
#Problem 5
def makeNegative():
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    newColor = makeColor(255-getRed(p),255-getGreen(p),255-getBlue(p))
    setColor(p, newColor)
  repaint(pic)
  
#Problem 6
def BnW():
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    avg_color = (getRed(p)+getGreen(p)+getBlue(p))/3.0
    newColor = makeColor(avg_color,avg_color,avg_color)
    setColor(p, newColor)
  repaint(pic)
 
def betterBnW():
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    avg_color = avg_color = (getRed(p)*.299 + getGreen(p)*.587 + getBlue(p)*.114)
    newColor = makeColor(avg_color,avg_color,avg_color)
    setColor(p, newColor)
  repaint(pic)