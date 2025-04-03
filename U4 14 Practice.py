"""
#1
for n in range(1,51,1):
  print(n,end=" ")

print()
print()

for n in range(50,0,-1):
  print(n,end=" ")

print()

#2
myInt = [2,4,6,8]
print(myInt)
print(len(myInt))
myInt.append(5)
myInt.append(10)
print(myInt)
print(len(myInt))
print(myInt[0])
print(myInt[-1])

print()

#3
names = ["John","Amy","Lance","Stacy"]
for n in names:
  print(n)
print()
for n in range(len(names)-1,-1,-1):
  print(names[n])
print()
for n in names:
  if n[0]=="A":
    print(n)

print()

#4
word = input("Enter a word: ")
def counter(word):
  count = 0
  for ltr in word:
    if ltr == "a":
      count+=1
  return count
print(counter(word))

print()
"""
#5
myString = "JCP is great"
print(myString[0])
print(myString[len(myString)-1])
otherString = myString[4:]
print(otherString)
someWords = myString.split()
print(someWords)
for word in someWords:
  if len(word)>=3:
    print(word)
