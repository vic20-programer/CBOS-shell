from datetime import datetime
from datetime import date
from os import system, name
import time
action = 0
num1 = 0
num2 = 0
operator = 0
result = 0
selected_slot = 1
Read = "a"

c = datetime.now()

if name == 'nt':
    _ = system('cls')
else:
    _ = system('clear')

print()
print("   __________  ____  _____    __             __  ____ __              _____       ______ ")
print("  / ____/ __ )/ __ \/ ___/   / /_  __  __   /  |/  (_) /_____  __  __/ ___/____  / __/ /_")
print(" / /   / __  / / / /\__ \   / __ \/ / / /  / /|_/ / / //_/ _ \/ / / /\__ \/ __ \/ /_/ __/")
print("/ /___/ /_/ / /_/ /___/ /  / /_/ / /_/ /  / /  / / / ,< /  __/ /_/ /___/ / /_/ / __/ /_  ")
print("\____/_____/\____//____/  /_.___/\__, /  /_/  /_/_/_/|_|\___/\__, //____/\____/_/  \__/  ")
print("                                /____/                      /____/                       ")
print()
print(" _       __     __                          __")
print("| |     / /__  / /________  ____ ___  ___  / /")
print("| | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \/ / ")
print("| |/ |/ /  __/ / /__/ /_/ / / / / / /  __/_/  ")
print("|__/|__/\___/_/\___/\____/_/ /_/ /_/\___(_)   ")
print("                                              ")
time.sleep(5)

if name == 'nt':
    _ = system('cls')
else:
    _ = system('clear')

print('Welcome to CBOS (Console Based Operating System) Ver 0.2 beta. Try Help to start')

print()

while True:
  action = input("What action ").title()
  if action == 'Time':
    print()
    current_time = datetime.now().strftime("%H:%M:%S")
    print('Current Time is:', current_time)
    print()
  if action == 'Date':
    print()
    today = date.today()
    print('Current Date:', today)
    print()
  if action == 'Calc':
    print()


    def add(x, y):
      return x + y


    def subtract(x, y):
      return x - y


    def multiply(x, y):
      return x * y


    def divide(x, y):
      return x / y

    while True:
      choice = input("Enter operator(+ - x /): ")

      if choice in ('+', '-', 'x', '/'):
        try:
          print()
          num1 = float(input("Enter first number: "))
          print()
          num2 = float(input("Enter second number: "))
        except ValueError:
          print()
          print("Invalid input. Please enter a number.")
          continue

        if choice == '+':
          print()
          print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '-':
          print()
          print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == 'x':
          print()
          print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '/':
          print()
          print(num1, "/", num2, "=", divide(num1, num2))

        print()
        next_calculation = input("New calculation? (y/n): ")
        print()
        if next_calculation == "n":
          break
      else:
        print()
        print("Invalid Input")
  if action == 'Help':
    print()
    print("commands for CBOS")
    print()
    print("action      command")
    print()
    print("calculator = Calc")
    print()
    print("date = Date")
    print()
    print("time = Time")
    print()
    print("notepad = Text Editor")
    print()
    print("Import app = Addcmd")
    print()
    print("Exit = quit")
    print()
  if action == 'Text Editor':
    print()
    selected_slot = int(input("what slot to select (1,2,3,4,5): "))
    print()
    Read = input("Read or write?: ").title()
    print()
    if Read == "Read":
      if selected_slot == 1:
        with open("slot1.txt", 'r') as file:
          print(file.read())
          print()
      if selected_slot == 2:
        with open("slot2.txt", 'r') as file:
          print(file.read())
          print()
      if selected_slot == 3:
        with open("slot3.txt", 'r') as file:
          print(file.read())
          print()
      if selected_slot == 4:
        with open("slot4.txt", 'r') as file:
          print(file.read())
          print()
      if selected_slot == 5:
        with open("slot5.txt", 'r') as file:
          print(file.read())
          print()
    if Read == "Write":
      if selected_slot == 1:
        with open("slot1.txt", 'w') as file:
          file.write(input("Enter your text here: "))
          print()
      if selected_slot == 2:
        with open("slot2.txt", 'w') as file:
          file.write(input("Enter your text here: "))
          print()
      if selected_slot == 3:
        with open("slot3.txt", 'w') as file:
          file.write(input("Enter your text here: "))
          print()
      if selected_slot == 4:
        with open("slot4.txt", 'w') as file:
          file.write(input("Enter your text here: "))
          print()
      if selected_slot == 5:
        with open("slot5.txt", 'w') as file:
          file.write(input("Enter your text here: "))
          print()
  if action == "Quit":
    if name == 'nt':
      _ = system('cls')
    else:
      _ = system('clear')
    print("   ______                ____               __")
    print("  / ____/___  ____  ____/ / /_  __  _____  / /")
    print(" / / __/ __ \/ __ \/ __  / __ \/ / / / _ \/ / ")
    print("/ /_/ / /_/ / /_/ / /_/ / /_/ / /_/ /  __/_/  ")
    print("\____/\____/\____/\__,_/_.___/\__, /\___(_)   ")
    print("                             /____/           ")
    time.sleep(5)
    if name == 'nt':
      _ = system('cls')
    else:
      _ = system('clear')
    break
  if action == "Addcmd":
      print()
      packagenamenopy = input("Input app name (without .py extention): ")
      packagename = packagenamenopy + ".py"
      print()
      cmdname = input("What command for this app? (calender could be cal, ect): ")
      print()
      with open("CBOS.py", 'r') as file:
          current_contents = file.readlines()
      current_contents.insert(0, "from appfolder " + "import " + packagenamenopy + '\n')
      with open("CBOS.py", 'w') as file:
          file.writelines(current_contents)
      with open("CBOS.py", 'a') as file:  # Open file in append mode
        file.write("  if action == " + "\"" + cmdname.title() + "\"" + ":\n")  # Write to file
        file.write("    " + packagenamenopy + ".launch()\n")  # Write second line

      print("App added successfully!")
      print("Please reboot to use the app")
      print()