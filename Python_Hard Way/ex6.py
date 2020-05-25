# Creates a variable and assigns a value to it
types_of_people = 10
#Assigns a string with f formating to a variable x
x = f"There are {types_of_people} types of people."

# similar cases as above
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"

# prints the strings saved in the variables x and y
print(x)
print(y)

# prints the strings x and y with some minor modifications
print(f"I said : {x}")
print(f"I also said: '{y}'")

# defines two variables and assigns the second variable with an f formatted string
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

#Used the format() function to compute the f formatted string
print(joke_evaluation.format(hilarious))

# Defines 2 string variables and their respective assignments
w = "This is left side of..."
e = "a string with a right side."

# String concatenation
print(w + e)