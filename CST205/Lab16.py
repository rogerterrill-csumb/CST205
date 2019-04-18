__author__ = "Roger Terrill, Abby Packham, Carlos Orduna"
__copyright__ = "Copyright 2019, CST205"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "rchicasterrill@csumb.edu, apackham@csumb.edu, cordunacorrales@csumb.edu  "
__status__ = "Production"

import urllib

def makePage():
  #replace the directory in the line below with the path to your file
  file = open("C:\\Developing\\School\\CST205\\superweb.html", "wt")
  file.write("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 
  Transition//EN" "http://www.w3.org/TR/html4/loose.dtd">
  
  <html>
  <head><title>I made this page with Python!</title>
  </head>
  <body>
  <h1>MY PYTHON PAGE!!!</h1>
  </body>
  </html>""")
  
  file.close()

def html_scrapper():
  file = open("C:\\Developing\\School\\CST205\\superweb.html", "wt")
  html_insert = ''
  header = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transition//EN" "http://www.w3.org/TR/html4/loose.dtd"> <html>'
  footer = '</html>'
  filehandle = urllib.urlopen("https://www.bbc.com/")
  read_data = filehandle.readlines()
  for line in range(len(read_data)):
    if '<li class="media-list__item' in read_data[line]:
      for i in range(3,28):
        html_insert += read_data[line+i]
  filehandle.close()
  print html_insert
  file.write(header + html_insert + footer)
  file.close()
