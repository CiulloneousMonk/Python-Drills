# Makes word "cars" the value of 100
cars = 100
# Makes space_in_a_car the value of 4 seats in a carpool
space_in_a_car = 4.0
# Makes word "drivers" the value of 30
drivers = 30
# Makes word "passengers" the value of 90
passengers = 90
# Makes phrase "cars_not_driven" calculate 100 - 30
cars_not_driven = cars - drivers
# Equates phrase cars_driven with drivers
cars_driven = drivers
# Makes phrase "carpool_capacity" calculate 30 times 4.0
carpool_capacity = cars_driven * space_in_a_car
# Makes phrase "average_passengers_per_car" calculate 90 divided by 30
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."