# Warm Up
def loop():
  word = ''
  while(word != 'stop'):
    word = requestString("Enter word")
    
    
def hangman():
  #showInformation("Today you play Hangman, type a letter and if it is in the word, the letter will be displayed, if not you lose a chance.")
  char = ''
  hidden_word = "star wars"
  length = len(hidden_word)
  guessed_letters = ''
  exposed_word = ""
  num_of_letters = 0
  num_of_letters_exposed = 0
  k = 6
  left_over = 0
  
  # Show underscore for characters in words
  for position in hidden_word:
    if position.isalpha():
      exposed_word = exposed_word + "_ "
      num_of_letters = num_of_letters + 1
    else:
      exposed_word = exposed_word + "  "
 
  # Ask for user input and search for character
  while true:
    char = requestString("What is your guess?").lower()[:1]
    if char.isalpha() == False:
      print "Letters only please!"
    count = 0
    if char in exposed_word or char in guessed_letters:
      print "You've already selected that letter, try again."
    elif char in hidden_word:
      print "Correct!"
      count = hidden_word.count(char)
      num_of_letters_exposed = num_of_letters_exposed + count
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
    if num_of_letters == num_of_letters_exposed:
      print "Congratulations you win!"
      return
    if k == 0:
      print "Sorry, you lose. Better luck next time!"
      return    
