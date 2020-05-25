from sys import argv

# Function definition that accepts two variables and prints them out with formatting
def cheeseAndCrackers(cheeseCount, boxesOfCrackers):
	print(f"You have {cheeseCount} cheeses!")
	print(f"You have {boxesOfCrackers} boxes of crackers!")
	print("Man that's enough for a party!")
	print("Get a blanket.\n")

script, cheese, crackers = argv

# Calls the function using values directly
print("We can just give the function numbers directly: ")
cheeseAndCrackers(20, 30)

# Calls the function using variables with assigned values
print("OR we can use variables from our script : ")
amountOfCheese = 10
amountOfCrackers = 50

cheeseAndCrackers(amountOfCheese, amountOfCrackers)

# Calls the funtion with values calculated while function call
print("We can even do math inside too: ")
cheeseAndCrackers(10 + 20, 5 + 6)

# Calls the function with values calculated during function call using variables
print("And we can combine the two variables and math: ")
cheeseAndCrackers(amountOfCheese + 100, amountOfCrackers + 1000)

# Calls the function using input from the user
cheeseAndCrackers(input("Enter the no. of cheese: "), input("Enter the no of crackers: "))

# Using argv while calling the function
cheeseAndCrackers(cheese, crackers)

# Calls the function using input from user and mathematical operation
cheeseAndCrackers(int(input("Cheese: ")) + 25, int(input("Crackers: ")) + 30)