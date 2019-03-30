
# Warm Up
def loop():
  word = ''
  while(word != 'stop'):
    word = requestString("Enter word")
    
    
def hangman():
  #showInformation("Today you play Hangman, type a letter and if it is in the word, the letter will be displayed, if not you lose a chance.")
  char = ''
  hidden_word = "star wars clone wars"
  length = len(hidden_word)
  exposed_word = ""
  k = 6
  
  # Show underscore for characters in words
  for position in hidden_word:
    if position.isalpha():
      exposed_word = exposed_word + "_ "
    else:
      exposed_word = exposed_word + "  "
 
  
  # Ask for user input and search for character
  while(char != 'z' and k > 0):
    print "Word so far:"
    print exposed_word
    char = requestString("What is your guess?").lower()
    if char.isalpha() == False:
      print "Letters only please!"
    count = 0
    if char in hidden_word:
      count = hidden_word.count(char)
      index = -1
      for i in range(count):
        index = hidden_word.find(char, index+1)
        print index
        exposed_word = exposed_word[:index*2] + char + exposed_word[index*2+1:]
    elif (char.isalpha()):
      print "Incorrect!"
      k = k - 1
      left_over = 6 - k
      print "You have used " + str(left_over) + " of six guesses\n"
      if k == 0:
        print "Sorry you ran out of guesses"
        return
    print exposed_word  
    
