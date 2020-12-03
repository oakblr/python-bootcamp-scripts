print("Character Deleting Bot")
print("----------------------\n")

from time import sleep

def characterRemover(text, character):
  finalText = ""
  for i in text:
    if(i != character):
      finalText = finalText + i
  return finalText

text = input("What is the text you want to remove charecters from?\n")
char1 = input("\nWhat charecter do you want to try removing from the text?\n")
char2 = input("\nWhat is annother charecter you want to try removing from the text?\n")

print("\nEdited Text:\n")
sleep(1)
print("\nWith " + char1 + " removed:\n")
print(characterRemover(text, char1) + "\n")
sleep(1)
print("With " + char2 + " removed:\n")
print(characterRemover(text, char2) + "\n")
sleep(1)
print("\nDone!")