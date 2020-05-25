cars = 100 													# Assigns the value 100 to the variable cars, to indicate the number the of cars
space_in_a_car = 4 											# Assigns the value 4 to variable 'space_in_a_car' to indicate the carrying capacity of the car
drivers = 30 												# Used to indicate the number of drivers available
passengers = 90 											# Used to indicate the number of passengers available
cars_not_driven = cars - drivers 							# Used to compute the no of cars that is available or idle
cars_driven = drivers 										# Indicates the no of cars that are in use.
carpool_capacity = cars_driven * space_in_a_car				# Calculates the no of people can be transported
average_passengers_per_car = int(passengers / cars_driven)	# Calculates the no of passengers travelling per car

# The following statements prints out the above values with meaningful sentences
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")