print("Lucky Number Game")
print("----------------------\n")

# Change theese to whatever you want
luckyNumber = 7
tries = 10

for i in range(tries):
  guess = input("What's my lucky number? \n")
  print("\nThat's " + str(guess == str(luckyNumber)) + "\n")