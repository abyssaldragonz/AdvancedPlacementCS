#initializing

#function
def showMenu():
  print("*"*55)
  print("*** AP COMPUTER SCIENCE PRINCIPLES CARD TERM TESTER ***")
  print("*"*55)
  print()
  print("Which section of cards would you like to practice?")
  print("=====")
  print("-1. Quit \n1. Cards 1-5 \n2. Cards 6-10 \n3. Cards 11-15")
  print()

def askAndCheck(q,a):
  wrong = 0
  correct = 0
  for i in range(len(q)):
    ans = input(q[i])
    ans = ans.lower()
    if ans == a[i]:
      print("correct")
      correct+=1
    else:
      print("wrong")
      wrong+=1
      print("the correct answer is:", a[i])
    print()
  print("Correct:",correct," | Wrong:",wrong)

def cards1To5():
  questions = []
  answers = ["human","computer","sequencing","efficient"]
  questions.append("language that has many words, many meanings, and is context dependent is called natural or _ language : ")
  #human
  questions.append("language that has few words and one literal meaning for each word is called _ language: ")
  #computer
  questions.append("the general term in which program statements are executed line by line: ")
  #sequencing
  questions.append("the smaller number of program statements, the more _ the program is: ")
  #efficient
  askAndCheck(questions,answers)

def cards6To10():
  questions = []
  answers = ["procedure","application programming interface","top-down design","iteration","pseudocode"]
  questions.append("another name for a function is: ")
  #procedure
  questions.append("a set of commands and rules for a particular application; API: ")
  #application programming interface
  questions.append("an approach of writing software with a general overview that then breaks down into a more detailed subgoals (w/ a dash): ")
  #top-down design
  questions.append("another term for a loop: ")
  #iteration
  questions.append("an informal programming language that is used to describe what an actual program would do: ")
  #pseudocode
  askAndCheck(questions,answers)

def cards11To15():
  questions = []
  answers = ["abstraction","","","",""]
  questions.append("making something simple to hide something more complex")
  #abstraction
  questions.append("")
  #
  questions.append("")
  #
  questions.append("")
  #
  questions.append("")
  #
  askAndCheck(questions,answers)

def cards15To20():
  questions = []
  answers = ["","","","",""]
  questions.append("")
  #
  questions.append("")
  #
  questions.append("")
  #
  questions.append("")
  #
  questions.append("")
  #
  askAndCheck(questions,answers)


"""
def cards#To#():
  questions = []
  answers = ["","","","",""]
  questions.append("")
  #
  questions.append("")
  #
  questions.append("")
  #
  questions.append("")
  #
  questions.append("")
  #
  askAndCheck(questions,answers)
"""
  
#main
choice = 0
while choice != -1:
  showMenu()
  choice = int(input("Which section would you like? Enter -1 to quit: "))
  if choice == 1:
    cards1To5()
  elif choice == 2:
    cards6To10()
  elif choice == 3:
    cards11To15()
  elif choice == 4:
    cards15To20()
  print()
print("Thank you for using the Card Term Tester.")