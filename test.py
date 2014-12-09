import math

number_to_change = float(input("Please enter a number to 3 or more decimal places: "))
#Get a number from user with 3 decimal places
print(number_to_change)
number_one = math.trunc(number_to_change)
#Take the users inputed number and return it to an integer
print(number_one)
number_two = round(number_to_change,2)
#
print(number_two)
print("The integer part of your number is {0}.".format(number_one))
print("The number to two decimal places is {0}.".format(number_two))
