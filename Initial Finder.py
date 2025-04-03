names=[]
initials=[]

#functions
def nameSearcher(names, initial):
  for n in range (len (names) ):
    fullName = names[n];
    
    NAME = fullName.split();
    firstName = NAME[0];
    secondName = NAME[1];
    
    firstIn = firstName[0];
    secondIn = secondName[0];
    INIT = firstIn + secondIn;

    print(INIT)
    
    for x in range(len (initial) ):
      if INIT == initial[x]:
        print(fullName + " is found at position " + n)
      else: 
        print("No match was found.  ")
      x+=1
    
    n+=1
  
#main
name = input("Enter a name (type '123' to quit): ");
while name != "123": 
  name = name.upper();
  names.append(name);
  name = input("Enter a name (type '123' to quit): ");

print();
initial = input("Enter an initial to search for (type '123' to quit): ");
while initial != "123": 
  initial = initial.upper();
  initials.append(initial);
  initial = input("Enter an initial to search for (type '123' to quit): ");

print();


print(names)
print(initial)
nameSearcher(names,initial)