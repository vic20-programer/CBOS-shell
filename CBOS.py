import ctypes
import sys
from datetime import datetime
from datetime import date
from os import system, name
import playsound
import os
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

time.sleep(.15)
print()
time.sleep(.25)
print("   __________  ____  _____    __             __  ____ __              _____       ______ ")
time.sleep(.25)
print("  / ____/ __ )/ __ \/ ___/   / /_  __  __   /  |/  (_) /_____  __  __/ ___/____  / __/ /_")
time.sleep(.25)
print(" / /   / __  / / / /\__ \   / __ \/ / / /  / /|_/ / / //_/ _ \/ / / /\__ \/ __ \/ /_/ __/")
time.sleep(.25)
print("/ /___/ /_/ / /_/ /___/ /  / /_/ / /_/ /  / /  / / / ,< /  __/ /_/ /___/ / /_/ / __/ /_  ")
time.sleep(.25)
print("\____/_____/\____//____/  /_.___/\__, /  /_/  /_/_/_/|_|\___/\__, //____/\____/_/  \__/  ")
time.sleep(.25)
print("                                /____/                      /____/                       ")
time.sleep(.15)
print()
time.sleep(.25)
print(" _       __     __                          __")
time.sleep(.25)
print("| |     / /__  / /________  ____ ___  ___  / /")
time.sleep(.25)
print("| | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \/ / ")
time.sleep(.25)
print("| |/ |/ /  __/ / /__/ /_/ / / / / / /  __/_/  ")
time.sleep(.25)
print("|__/|__/\___/_/\___/\____/_/ /_/ /_/\___(_)   ")
print("                                              ")
playsound.playsound(os.path.join(os.path.dirname(__file__), "startup.wav"))

if name == 'nt':
    _ = system('cls')
else:
    _ = system('clear')

print('Welcome to CBOS (Console Based Operating System) Ver 0.2 beta. Try Help to start')

print()

while True:
  action = input("What command?: ").title()
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
    print("Import app = Add Command")
    print()
    print("File Explorer = Files")
    print()
    print("Grant Admin (needed for text editor and add command) = admin")
    print()
    print("Exit = quit")
    print()
  if action == 'Text Editor':
    print()
    if is_admin():
      admin = 1
    else:
      print("This app needs admin privileges please run the command admin to use this app.")
      print()
      break
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
    time.sleep(.25)
    print("  / ____/___  ____  ____/ / /_  __  _____  / /")
    time.sleep(.25)
    print(" / / __/ __ \/ __ \/ __  / __ \/ / / / _ \/ / ")
    time.sleep(.25)
    print("/ /_/ / /_/ / /_/ / /_/ / /_/ / /_/ /  __/_/  ")
    time.sleep(.25)
    print("\____/\____/\____/\__,_/_.___/\__, /\___(_)   ")
    time.sleep(.25)
    print("                             /____/           ")
    time.sleep(5)
    if name == 'nt':
      _ = system('cls')
    else:
      _ = system('clear')
    break
  if action == "Add Command":
      print()
      def is_admin():
        try:
          return ctypes.windll.shell32.IsUserAnAdmin()
        except:
          return False


      if is_admin():
        admin = 1
      else:
        print()
        print("This app needs admin privileges please run the command admin to use this app.")
        print()
        break
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
      print("Please reboot CBOS to use the app")
      print()

  if action == "Files":
    def list_directory(path):
      print(f"\nDirectory: {path}")
      try:
        for item in os.listdir(path):
          print("  -", item)
      except PermissionError:
        print("Permission denied.")
      except FileNotFoundError:
        print("Directory not found.")


    def read_text_file(path):
      try:
        with open(path, 'r') as file:
          print("\nFile Contents:\n")
          print(file.read())
      except Exception as e:
        print("Error reading file:", e)


    def rename_file(old_path, new_name):
      new_path = os.path.join(os.path.dirname(old_path), new_name)
      try:
        os.rename(old_path, new_path)
        print(f"Renamed to {new_path}")
      except Exception as e:
        print("Error renaming file:", e)


    def file_browser():
      current_path = input("Start at directory (e.g., C:\\ or /home): ").strip()
      while True:
        list_directory(current_path)
        print("\n🔧 Options: cd [dir], open [file], rename [file], drive [letter], quit")
        command = input("What next? ").strip().split(maxsplit=1)
        if not command:
          continue

        action = command[0].lower()
        arg = command[1] if len(command) > 1 else None

        if action == "cd" and arg:
          current_path = os.path.join(current_path, arg)
        elif action == "open" and arg:
          read_text_file(os.path.join(current_path, arg))
        elif action == "rename" and arg:
          old_file = os.path.join(current_path, arg)
          new_name = input("New name: ").strip()
          rename_file(old_file, new_name)
        elif action == "drive" and arg:
          current_path = f"{arg.upper()}:\\"
        elif action == "quit":
          print("Exiting browser.")
          break
        else:
          print("❓ Unknown or incomplete command.")


    file_browser()
  if action == "Admin":
    def is_admin():
      try:
        return ctypes.windll.shell32.IsUserAnAdmin()
      except:
        return False


    if is_admin():
      # Code to run with admin privileges
      print()
      print("Running as administrator")
      print()
    else:
      # Re-run the script with admin privileges
      ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, __file__, None, 1)
      break