__author__ = "Roger Terrill, Abby Packham, Carlos Orduna"
__copyright__ = "Copyright 2019, CST205"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "rchicasterrill@csumb.edu, apackham@csumb.edu, cordunacorrales@csumb.edu  "
__status__ = "Production"



def madlib(file):
    f = open(file,'r')
    read_data = f.read()
    f.close()
    word_hint = ['Enter a verb','Enter a thing','Enter a job title', 'Enter a verb', 'Enter a person', 'Enter and adjective', 'Enter a noun', 'Enter an adjective','Enter a noun', 'Enter an adjective','Enter a verb', 'Enter an adjective','Enter a thing','Enter an ajective','Enter an adjective']
    word_list =[]
    for i in range(15):
      word = requestString(word_hint[i]).upper()
      word_list.append(word)
      word_index = "[" + str(i+1) + "]" 
      read_data = read_data.replace(word_index, word)
    showInformation("****************Madlib Results!!!**************** \n" + read_data)
    

