"""
#1.
for letter in "HELLO":
  print(letter)

#2. 
message = input("Enter a message: ")
for letter in message:
  print(letter)
for letter in message:
  print(letter, end="-")

#3.
msg=input("Enter a message: ")
dupString = ""
for letter in msg:
  for i in range(2):
    dupString += letter
print(dupString)

#4.
#init
#function
def stars(num):
  retString = ""
  for i in range(num):
    retString+="*"
  return retString
#main
print(stars(10))
print(stars(50))

#5.
#init
#function
def stars(sym,num):
  retString=sym*num
  return retString
#main
print(stars("$",10))
print(stars("*",50))
"""