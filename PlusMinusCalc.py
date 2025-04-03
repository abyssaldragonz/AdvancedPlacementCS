#init


#func
def plusmin():
  by = int(input("plus/minus by how much?: "))
  list = []
  number = int(input("insert a number: "))
  list.append(number)
  while number != 0:
    number = int(input("insert a number: "))
    list.append(number)
  print()
  for x in list:
    print(x,"plus up by",by,"is . . . ",x+by)
    print(x,"minus down by",by,"is . . . ",x-by)
    print()

#main
plusmin()