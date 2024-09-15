import os

# Define the path for the CBOS folder on the C drive
folder_path = input("Input file path for example 'C:/CBOS': ")

# Create the folder
os.makedirs(folder_path, exist_ok=True)

# Read the code from code.txt
with open('code(npass).txt', 'r') as code_file:
    code_content = code_file.read()

# Create a Python file called CBOS.py in the CBOS folder and write the code to it
with open(os.path.join(folder_path, 'CBOS.py'), 'w') as py_file:
    py_file.write(code_content)

# Create 5 .txt files named slot1.txt to slot5.txt and write "hello" to each
for i in range(1, 6):
    with open(os.path.join(folder_path, f'slot{i}.txt'), 'w') as txt_file:
        txt_file.write('\n')

print("Setup complete!")
