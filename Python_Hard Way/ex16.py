from sys import argv

script, fileName = argv

print(f"We're going to erase {fileName}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(fileName, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I am gong to write these to the file.")

target.write(line1 + '\n'+ line2 + '\n' + line3 + '\n')

print("And finally we close it.")
target.close()

target = open(fileName)

print("The updated file contents are as follows : ")
print(target.read())

target.close()