
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
  guessed_letters = ''
  exposed_word = ""
  k = 6
  left_over = 0
  
  # Show underscore for characters in words
  for position in hidden_word:
    if position.isalpha():
      exposed_word = exposed_word + "_ "
    else:
      exposed_word = exposed_word + "  "
 
  # Ask for user input and search for character
  while(char != 'z'):
    char = requestString("What is your guess?").lower()
    if char.isalpha() == False:
      print "Letters only please!"
    count = 0
    if char in exposed_word or char in guessed_letters:
      print "You've already selected that letter, try again."
    elif char in hidden_word:
      print "Correct!"
      count = hidden_word.count(char)
      index = -1
      for i in range(count):
        index = hidden_word.find(char, index+1)
        exposed_word = exposed_word[:index*2] + char + exposed_word[index*2+1:]
    elif (char.isalpha()) and ((char in hidden_word) == false):
      k = k - 1
      left_over = 6 - k
      guessed_letters = guessed_letters[:left_over] + char
      
    print "Word so far:"
    print exposed_word
    print "Incorrect guesses:"
    print guessed_letters
    print "You have used " + str(left_over) + " of six guesses\n"
    if k == 0:
      print "Sorry, you lose. Better luck next time!"
      return    
