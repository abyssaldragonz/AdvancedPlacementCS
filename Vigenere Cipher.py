def encrypt():
  alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
  user = input("Enter a word or sentence to be encrypted into Vigenere Cipher: \n")
  user=user.lower()
  punt = []
  words = ""
  userCopy = user

  for i in range(len(user)):
    if user[i] not in alphabet:
      punt.append(i)
      userCopy = userCopy.replace(user[i],"")
  
  print(punt)
  print(userCopy)


  key = input("Enter the key: ")
  for i in range(len(userCopy)):
    msgIn = alphabet.find(userCopy[i])
    keyIn = alphabet.find(key[i % len(key)])    
    msgIn+=keyIn
    words+=alphabet[msgIn]

  for x in punt:
    words = words[:x] + user[x] + words[x:]

  print()
  print("The encoded message is...:")
  print(words)


def decrypt():
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  user = input("Enter a word or sentence to be decrypted from Vigenere Cipher: \n")
  user=user.lower()
  punt = []
  words = ""
  userCopy=user

  for i in range(len(user)):
    if user[i] not in alphabet:
      punt.append(i)
      userCopy = userCopy.replace(user[i],"")

  key = input("Enter the key: ")
  for i in range(len(userCopy)):
    msgIn = alphabet.find(userCopy[i])
    keyIn = alphabet.find(key[i % len(key)])    
    msgIn-=keyIn
    words+=alphabet[msgIn]

  for x in punt:
    words = words[:x] + user[x] + words[x:]

  print()
  print("The encoded message is...:")
  print(words)

encrypt()
decrypt()

