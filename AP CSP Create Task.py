#INITIALIZING
import random
colors = ["red","orange","yellow","green","blue","purple"]
guessesLeft = 10
black = 0
code = []


#FUNCTIONS
"""
function name : checkGuess
description : takes the user's guess and checks it with the secret code
parameters : 
  user - user's guess - list of strings
  secretCode - the secret code - list of strings
"""
def checkGuess(user, secretCode):
  black = 0
  white = 0
  indexes = []
  #checking for number of black key pegs
  #runs through code and guess and see if indexes match
  for i in range(len(secretCode)):
    if user[i] == secretCode[i]:
      black += 1
      indexes.append(i)
  #removing known black key pegs so duplicates don't occur
  for x in indexes[::-1]: 
    secretCode.pop(x)
    user.pop(x)
  #calculating number of white key pegs
  white = len(user)
  for w in range(len(secretCode)):
  #runs through list by removing first element every time
    if user[0] in secretCode:
      index = secretCode.index(user[0])
      secretCode.pop(index)
    else:
      white -= 1 
    user.pop(0)
  print("There are", black, "black key dots and", white, "white key dots.")
  #returns number correct to see if user is correct
  return black


#MAIN
print("*" * 29)
print("*** WELCOME TO MASTERMIND ***")
print("*" * 29)
print()
print(">> KEY << \nBLACK DOT: correct color in the correct position \nWHITE DOT: correct color but in the wrong position")
print("KEY DOTS ARE IN NO PARTICULAR ORDER")
print("*" * 30)
print("SLOTS: FOUR (4) \nCOLORS: red orange yellow green blue purple ")
print(">> YOU MUST HAVE FOUR (4) BLACK KEY DOTS TO WIN")
print(">> TYPE YOUR GUESS WITH SPACES IN BETWEEN EACH COLOR \n    (see COLORS for example) \n>> BE SURE TO TYPE FOUR(4) COLORS")
print("*" * 30)
#making secret code
for i in range(4):
  choose = random.choice(colors)
  code.append(choose)
print("SECRET CODE HAS BEEN CHOSEN \nYOU HAVE 10 GUESSES TO CRACK THE CODE. ")
print("*" * 30)
print()
#exits loop if guesses left is 0 or if number of correct (black) is 4
while guessesLeft != 0 and black!=4:
  userGuess = input("ENTER YOUR GUESS: ")
  userGuess = userGuess.lower()
  userGuess = userGuess.split()
  #make copy of secret code so the original code isn't altered
  codeCopy = code.copy()
  #calls function and stores the return as black
  black = checkGuess(userGuess, codeCopy)
  guessesLeft -= 1
  print("You have",guessesLeft,"guesses left.")
  print()
print("*" * 30)
print()
#prints win or lose message in case user guesses correctly on last guess
if guessesLeft >=0 and black == 4:
  print("YOU WIN!")
elif guessesLeft == 0 and black < 4:
  print("YOU LOSE! \nTHE SECRET CODE WAS:",' '.join(code))
print()
print("*** THANK YOU FOR PLAYING MASTERMIND ***")