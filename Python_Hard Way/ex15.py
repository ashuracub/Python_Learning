# imports the argv function to get values from the user on running the script
from sys import argv

# Assigns the input from the user to the variables script (which is basically the script name), and the other value to the filename variable
script = argv

filename = input("Enter the filename\n> ")

# Opens the file in the same directory with the same name as given in the argument and assigns it to the variable txt. Make sure there exists a file with the same name in the directory
txt = open(filename)

# Prints out the contents of the file name using the function read()
print(f"Here's you file {filename}")
print(txt.read())

# Closes the file
txt.close()