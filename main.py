from time import sleep
def main():
  print("Codefest 2020 Bootcamp: Example Python Programs")
  print("-------------------------------------------------\n")

  delay = 1.3
  
  while True:
    print("Select your level:\n")
    print("1. Beginner")
    print("2. Intermediate\n")
    print("Enter Q to quit\n")

    level = input("")

    sleep(delay)

    if(level == "1"):
      print("\n-------------------------------------------------\n")
      
      while True:
        print("Type in the first letter of the program you want to run:\n")
        print(" - a_input_script.py")
        print(" - b_for_script.py")
        print(" - c_if_script.py")
        print(" - d_while_script.py")
        print(" - e_functions_script.py")
        print(" - f_returning_values_script.py\n")
        print("Enter B to go back\n")

        level = input("")

        sleep(delay)

        if(level == "a"):
          print("\n-------------------------------------------------")
          exec(open("Beginner/a_input_script.py").read())
          print("\n-------------------------------------------------\n")

        elif(level == "b"):
          print("\n-------------------------------------------------")
          exec(open("Beginner/b_for_script.py").read())
          print("\n-------------------------------------------------\n")

        elif(level == "c"):
          print("\n-------------------------------------------------")
          exec(open("Beginner/c_if_script.py").read())
          print("\n-------------------------------------------------\n")

        elif(level == "d"):
          print("\n-------------------------------------------------")
          exec(open("Beginner/d_while_script.py").read())
          print("\n-------------------------------------------------\n")

        elif(level == "e"):
          print("\n-------------------------------------------------")
          exec(open("Beginner/e_functions_script.py").read())
          print("\n-------------------------------------------------\n")

        elif(level == "f"):
          print("\n-------------------------------------------------")
          exec(open("Beginner/f_returning_values_script.py").read())
          print("\n-------------------------------------------------\n")

        elif(level == "B"):
          break

        else:
          print("\n-------------------------------------------------")
          print("\nType in a letter or B")
          print("\n-------------------------------------------------\n")

      sleep(delay)

      print("\n-------------------------------------------------\n")

    elif(level == "2"):
      print("\n-------------------------------------------------\n")
      
      while True:
        print("Type in the first letter of the program you want to run:\n")
        print(" - a_input_script.py")
        print(" - b_for_script.py\n")
        print("Enter B to go back\n")

        level = input("")

        sleep(delay)

        if(level == "a"):
          print("\n-------------------------------------------------")
          exec(open("Intermediate/a_input_script.py").read())
          print("\n-------------------------------------------------\n")

        elif(level == "b"):
          print("\n-------------------------------------------------")
          exec(open("Intermediate/b_for_script.py").read())
          print("\n-------------------------------------------------\n")

        elif(level == "B"):
          break

        else:
          print("\n-------------------------------------------------")
          print("\nType in a letter or B")
          print("\n-------------------------------------------------\n")

      sleep(delay)

      print("\n-------------------------------------------------\n")

    elif(level == "Q"):
      print("\n-------------------------------------------------")
      print("\nGoodbye!")
      break

    else:
      print("\n-------------------------------------------------")
      print("\nType in 1, 2, or Q")
      print("\n-------------------------------------------------\n")
    
    sleep(delay)

if(__name__ == "__main__"):
  main()