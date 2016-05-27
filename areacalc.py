#!/usr/bin/python

# import the needed Python code
from math import pi
from time import sleep
from datetime import datetime
from sys import stdout

# make datetime a variable and print the app name and current date and time.
now = datetime.now()

print("Welcome to the Super Simple Area Calculator!")
sleep(0.5)
print("The current date and time is %s/%s/%s %s:%s") % (now.month, now.day, now.year, now.hour, now.minute)

# use sleep to simulate a "thinking" calculator
sleep(1)

# Can't forget correct units!
hint = "Don't forget to include the correct units! \nExiting...\n"

# time to get user input and calculate the area for their selection
print("(C)ircle")
sleep(.25)
print("(T)riangle")
sleep(.25)
print("(S)quare or Rectangle")
sleep(.25)
print("(R)hombus")
sleep(.25)
print("(Tr)apezoid")
sleep(.25)
option = raw_input("Please enter one of the preceding otions: ")
option = option.upper()

# the area of a circle is pi * radius squared
if option == "C" or option == "Circle":
	radius = float(raw_input("Enter the radius of the circle: "))
	area = pi * radius ** 2
	print("The pie is baking...")
	sleep(1)
	print("Area: %.2f. \n%s" % (area, hint))
# the area of a triangle is .5 * base * height, or
# base * height / 2
elif option == "T" or option == "Triangle":
	base = float(raw_input("Enter the base of the triangle: "))
	height = float(raw_input("Enter the height of the triangle "))
	area = base * height / 2
	print("Uni, Bi, Tri...")
	sleep(1)
	print("Area: %.2f. \n%s" % (area, hint))
elif option == "S" or option == "Square" or option == "Rectangle":
	base = float(raw_input("Enter the base of the square or rectangle: "))
	height = float(raw_input("Enter the height of the square or rectangle: "))
	area = base * height
	print("We're squaring up your answer...")
	sleep(1)
	print("Area: %.2f. \n%s" % (area, hint))
elif option == "R" or option == "Rhombus":
	diagonal_1 = float(raw_input("Enter diagonal 1 of the rhombus: "))
	diagonal_2 = float(raw_input("Enter diagonal 2 of the rhombus: "))
	area = diagonal_1 * diagonal_2 / 2
	print("Pulling the rhombus into the station...")
	sleep(1)
	print("Area: %.2f. \n%s" % (area, hint))
elif option == "Tr" or option == "Trapezoid":
	base_1 = float(raw_input("Enter the first base of the trapezoid: "))
	base_2 = float(raw_input("Enter the second base of the trapezoid: "))
	height = float(raw_input("Enter the height of the trapezoid: "))
	area = (base_1 + base_2) / 2 * height
	print("Super-shape extrodinaire! Trapezoid! Trapezoid!")
	sleep(1)
	print("... Uh, never mind ...")
	sleep(1)
	print("Area: %.2f. \n%s" % (area, hint))
# and an else statement in case the user inputs garbage
else:
	print("Error! Invalid shape specified. Exiting...")
	
