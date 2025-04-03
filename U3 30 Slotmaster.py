#initializing
import random
num = 0
winPull = 0
losePull = 0


#function
def asterik():
  print()
  print("*"*25)
  print()

def slotMaster(money,winPull,losePull):
  symbols = ["♠","♥","♣","♦"]
  result = ""
  for i in range(3):
    result += random.choice(symbols)
  print("The result is:",result)

  add = 0
  if result == "♠♠♠":
    add = pull * 5
  elif result == "♥♥♥":
    add = pull * 4
  elif result == "♣♣♣":
    add = pull * 3
  elif result == "♦♦♦":
    add = pull * 2
  elif result == "♠♥♣" or result == "♥♣♦" or result == "♦♣♥" or result == "♣♥♠":
    add = pull
  else:
    add = pull * (-1)
  
  if add >= 0:
    print("You won $",add)
    winPull += 1
  if add < 0:
    print("You lost $",add)
    losePull += 1
  money += add
  return money, winPull, losePull


#main
print("*"*25)
print("* Welcome to SLOTMASTER *")
print("*"*25)
print()
print("*******___PRIZES___******")
print(" ♠♠♠ = wins 5x pull")
print(" ♥♥♥ = wins 4x pull")
print(" ♣♣♣ = wins 3x pull")
print(" ♦♦♦ = wins 2x pull")
print(" card symbols in order (♠♥♣ or ♥♣♦ or ♦♣♥ or ♣♥♠) = wins pull")
print(" everything else = loses pull")
print("*"*25)
print()

print()
name = input("What is your name? ")
print("Welcome to the casino,",name,". You have a nice name. Unique!")
print("Why don't you try your hand and luck at the Rising Red?")

print()
startMoney = int(input("How much are you willing to bet? : $ "))
endMoney = startMoney
if startMoney >= 1500:
  print("$",startMoney,"? Confident, are you? Go right on ahead.")
else:
  print("$",startMoney,"is not a lot, but you do you, I guess.")

pull = int(input("How much are you willing to pull each turn? : $ "))
if pull >= 500:
  print("Go big or go home, I suppose.")
else:
  print("Playing safe, eh?")

print()
print("Okay. Let us get started.")
asterik()

play = input("Please insert 'p' to pull. Insert 'q' to quit: ")
while play != "q":
  num += 1
  endMoney,winPull,losePull = slotMaster(endMoney,winPull,losePull)
  print("You currently have $", endMoney)
  print()
  play = input("Please insert 'p' to pull. Insert 'q' to quit: ")

asterik()
print("You started with $",startMoney,"and ended with $",endMoney,".")
print("You pulled", num,"times.")
print(winPull,"of your",num," pulls are wins.")
print(losePull,"of your",num,"pulls are loses.")

print()
if startMoney > endMoney:
  print("Better luck next time. You lost money.")
elif startMoney < endMoney:
  print("Increadible luck! You won money.")  
if endMoney < 0:
  print("Better go find a job sooner than later.")
else:
  print("Eh. At least you didn't lose any money, only time.")

asterik()
print("Win or lose, I hope you had fun at the Rising Red. Have a good rest of your day.")
