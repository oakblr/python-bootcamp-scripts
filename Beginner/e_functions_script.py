print("Square Drawing Bot")
print("----------------------\n")

from time import sleep

def squareDrawer(size):
  for i in range(size):
    for i in range(size):
      print("0", end=" ")
      sleep(0.005)
    print("")

size1 = input("What should the size of the first square be? \n")
size2 = input("\nWhat should the size of the second square be? \n")
size3 = input("\nWhat should the size of the third square be? \n")

print("\nGenerating Squares...\n")
sleep(1)
print("\nSquare 1:\n")
squareDrawer(int(size1))
print("\nSquare 2:\n")
squareDrawer(int(size2))
print("\nSquare 3:\n")
squareDrawer(int(size3))
print("\nDone!")