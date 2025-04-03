#initializing

#functions
def charEn():
	print("KEY:")
	print("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")
	print("! @ # $ % ^ & * ( ) _ + 1 2 3 4 5 6 7 8 9 0 - = > <")
	orig = "abcdefghijklmnopqrstuvwxyz"
	alphabet = "!@#$%^&*()_+1234567890-=><"
	c = input("Enter a word or sentence to be encrypted into a Character Substitution: \n")
	c=c.lower()
	words = ""
	for i in range(len(c)):
		if c[i] in orig:
			index = orig.find(c[i])    
			words+=alphabet[index]
		else:
			words+=c[i]
	print()
	print("The encoded message is...:")
	print(words)

def charDe():
	print("KEY:")
	print("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")
	print("! @ # $ % ^ & * ( ) _ + 1 2 3 4 5 6 7 8 9 0 - = > <")
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	orig = "!@#$%^&*()_+1234567890-=><"
	c = input("Enter a word or sentence to be decrypted into a Character Substitution: \n")
	c=c.lower()
	words = ""
	for i in range(len(c)):
		if c[i] in orig:
			index = orig.find(c[i])    
			words+=alphabet[index]
		else:
			words+=c[i]
	print()
	print("The decoded message is...:")
	print(words)

def reverser():
  r = input("Enter a word or sentence to be reversed: ")
  revSent = ""
  revSent += r[::-1]
  print()
  print("The message is...:")
  print(revSent)

def pigLatinEn():
  p = input("Enter a word or sentence to be encrypted into Pig Latin: \n")
  p=p.lower()
  p=p.split()
  vowels = "aeiou"
  words=""
  index=0
  for w in p:
    for i in range (len(w)):
      if w[i] in vowels:
        index=i
        break
    w = w[index:] + w[0:index] + "ay "
    words+=w
  print()
  print("The encoded message is...:")
  print(words)

def pigLatinDe():
  list = ["spr","str","spl","chr","shr","thr","bl", "br", "cl", "cr", "dr", "fl", "fr", "gl", "gr", "pl", "pr", "sc", "sk", "sl", "sm", "sn", "sh", "sp", "st", "sw", "tr", "th","tw","qu"]
  d = input("Enter a word or sentence to be decrypted from Pig Latin: \n")
  words=""
  index = 1
  d = d.lower()
  d = d.split() 
  for w in d:
    w=w[:-2]
    for i in range(len(list)):
      if list[i] in w:
        index = len(list[i])
        break
      else:
        index = 1
    w = w[-index:] + w[:-index] + " "
    words+=w
  print()
  print("The decoded message is...:")
  print(words)

def caesarEn():
  alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
  c = input("Enter a word or sentence to be encrypted into Caesar Shift: \n")
  c=c.lower()
  words = ""
  s = int(input("Enter a number to shift by: "))
  for i in range(len(c)):
    if c[i] in alphabet:
      index = alphabet.find(c[i])    
      index+=s
      words+=alphabet[index]
    else:
      words+=c[i]
  print()
  print("The encoded message is...:")
  print(words)

def caesarDe():
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  c = input("Enter a word or sentence to be decrypted from Caesar Shift: \n")
  c=c.lower()
  words = ""
  s = int(input("Enter the shift: "))
  for i in range(len(c)):
    if c[i] in alphabet:
      index = alphabet.find(c[i])    
      index-=s
      words+=alphabet[index]
    else:
      words+=c[i]
  print()
  print("The decoded message is...:")
  print(words)

def vigEn():
  alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
  user = input("Enter a word or sentence to be encrypted into Vigenere Cipher: \n")
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
    msgIn += keyIn
    words += alphabet[msgIn]
  for x in punt:
    words = words[:x] + user[x] + words[x:]
  print()
  print("The encoded message is...:")
  print(words)

def vigDe():
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
    msgIn -= keyIn
    words += alphabet[msgIn]
  for x in punt:
    words = words[:x] + user[x] + words[x:]
  print()
  print("The decoded message is...:")
  print(words)

def hexEn():
  orig = [" ","!","\"","#","$","%","&","\'","(",")","*","+",",","-",".","/","0","1","2","3","4","5","6","7","8","9",":",";","<","=",">","?","@","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","[",'\\',']',"^","_","`","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","{","|","}","~"]
  hexes = ["20","21","22","23","24","25","26","27","28","29","2A","2B","2C","2D","2E","2F","30","31","32","33","34","35","36","37","38","39","3A","3B","3C","3D","3E","3F","40","41","42","43","44","45","46","47","48","49","4A","4B","4C","4D","4E","4F","50","51","52","53","54","55","56","57","58","59","5A","5B","5C","5D","5E","5F","60","61","62","63","64","65","66","67","68","69","6A","6B","6C","6D","6E","6F","70","71","72","73","74","75","78","77","78","79","7A","7B","7C","7D","7E"]
  c = input("Enter a word or sentence to be encrypted into Hexademical: \n")
  words = ""
  for i in range(len(c)):
    if c[i] in orig:
      index = orig.index(c[i])
      words+=hexes[index]+" "
    else:
      words+=c[i]+" "
  print()
  print("The encoded message is...:")
  print(words)

def hexDe():
  hexes = [" ","!","\"","#","$","%","&","\'","(",")","*","+",",","-",".","/","0","1","2","3","4","5","6","7","8","9",":",";","<","=",">","?","@","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","[",'\\',']',"^","_","`","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","{","|","}","~"]
  orig = ["20","21","22","23","24","25","26","27","28","29","2A","2B","2C","2D","2E","2F","30","31","32","33","34","35","36","37","38","39","3A","3B","3C","3D","3E","3F","40","41","42","43","44","45","46","47","48","49","4A","4B","4C","4D","4E","4F","50","51","52","53","54","55","56","57","58","59","5A","5B","5C","5D","5E","5F","60","61","62","63","64","65","66","67","68","69","6A","6B","6C","6D","6E","6F","70","71","72","73","74","75","78","77","78","79","7A","7B","7C","7D","7E"]
  c = input("Enter a word or sentence to be decrypted into Hexademical: \n")
  c=c.split()
  words = ""
  for i in range(len(c)):
    if c[i] in orig:
      index = orig.index(c[i])
      words+=hexes[index]
    else:
      words+=c[i]
  print()
  print("The decoded message is...:")
  print(words)

#main
print("**********************************")
print("*** Welcome to the CryptMaster ***")
print("**********************************")
print()
print("-1. Quit \n1. Character Substitution Encrypter \n2. Character Substitution Decrypter \n3. Reverser \n4. Pig Latin Encrypter \n5. Pig Latin Decrypter \n6. Caesar Shift Encrypter \n7. Caesar Shift Decrypter \n8. Vigenere Cipher Encrypter \n9. Vigenere Cipher Decrypter \n10. Hexadecimal Encrypter \n11. Hexadecimal Decrypter")
print()
choice = int(input("Which crypt would you like?: "))
print()

while choice != -1:
	print("**********************************")
	print()
	if choice == 1:
		print("*** CHARACTER SUBSTITUTION ENCRYPTER ***")
		charEn()
	elif choice == 2:
		print("*** CHARACTER SUBSTITUTION DECRYPTER ***")
		charDe()
	elif choice == 3:
		print("*** REVERSER ***")
		reverser()
	elif choice == 4:
		print("*** PIG LATIN ENCRYPTER ***")
		pigLatinEn()
	elif choice == 5:
		print("*** PIG LATIN DECRYPTER ***")
		pigLatinDe()
	elif choice == 6:
		print("*** CAESAR SHIFT ENCRYPTER ***")
		caesarEn()
	elif choice == 7:
		print("*** CAESAR SHIFT DECRYPTER ***")
		caesarDe()
	elif choice == 8:
		print("*** VIGENERE CIPHER ENCRYPTER ***")
		vigEn()
	elif choice == 9:
		print("*** VIGENERE CIPHER DECRYPTER ***")
		vigDe()
	elif choice == 10:
		print("*** HEXADECIMAL DECRYPTER ***")
		hexEn()
	elif choice == 11:
		print("*** HEXADECIMAL DECRYPTER ***")
		hexDe()      
	else:
		print("Please select a crypt or enter -1 to quit.")
	print()
	print("**********************************")
	print()
	choice = int(input("Which crypt would you like?: "))
print()
print("**********************************")
print()
print("Thank you for using the CryptMaster.")	
