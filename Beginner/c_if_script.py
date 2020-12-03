print("Lucky Number Game 2")
print("----------------------\n")

# Change theese to whatever you want
luckyNumber = 7
tries = 10

for i in range(tries):
  guess = input("What's my lucky number? \n")

  if(guess == str(luckyNumber)):
    print("\nThat's Correct!")
    print("\nCongratulations, you win!")
    break

  else:
    if(int(guess) > luckyNumber):
      print("\nToo Large!\n")

    else:
      print("\nToo Small!\n")