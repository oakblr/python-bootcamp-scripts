print("Annoy Bot")
print("----------------------\n")

from random import randint

over = False

while(not over):
  x = randint(0, 100)
  y = randint(0, 100)

  userInput = input("Do you want to know what's " + str(x) + " + " + str(y) + "? (y/n)\n")

  if(userInput == "y"):
    print("\nIt's " + str(x + y))
    print("\nGoodbye!")
    over = True

  elif(userInput == "n"):
    print("\nIt's " + str(x + y) + " BTW\n")
  
  else:
    print("\ny or n, please!\n")