#################################################################
#					 A Simple Area Calculator 					#
#						(with slow typing)						#
#																#
# 	A simple calculator that finds the area for a variety of 	#
#		 		different shapes. That's about it.	 			#
#																#
#  This program and its source are 100% libre. You are FREE to 	#
# run, study, share (copy), and modify this software so long as #
# 		these rights are retained in future incarnations. 		#
#						  Happy coding!							#
#																#
# Author: Hvitserk the Berserker & CodeCademy	  Copyleft 2016 #
#################################################################
#!/usr/bin/python

# import the needed Python code
from math import pi
from time import sleep
from datetime import datetime
from sys import stdout

# make datetime a variable and print the app name and current date and time.
def print_slow(str):
    for letter in str:
        stdout.write(letter)
        stdout.flush()
        sleep(0.06)

now = datetime.now()

print_slow("Welcome to the Super Simple Area Calculator!\n")
sleep(0.5)
print_slow("The current date and time is ")
sleep(0.5)
print("%s/%s/%s %s:%s\n") % (now.month, now.day, now.year, now.hour, now.minute)

# use sleep to simulate a "thinking" calculator
sleep(1)

# Can't forget correct units!
hint = "Don't forget to include the correct units! \nExiting...\n"

# time to get user input and calculate the area for their selection
print_slow("(C)ircle\n")
sleep(.25)
print_slow("(TRI)angle\n")
sleep(.25)
print_slow("(S)quare or Rectangle\n")
sleep(.25)
print_slow("(R)hombus\n")
sleep(.25)
print_slow("(TRA)pezoid\n")
sleep(.25)
option = raw_input("Please enter one of the preceding otions: ")
option = option.upper()

# the area of a circle is pi * radius squared
if option[0] == "C":
	radius = float(raw_input("Enter the radius of the circle: "))
	area = pi * radius ** 2
	print_slow("The pie is baking...\n")
	sleep(1)
	print_slow("Area: %.2f. \n%s" % (area, hint))
# the area of a triangle is .5 * base * height, or
# base * height / 2
elif option[0:3] == "TRI":
	base = float(raw_input("Enter the base of the triangle: "))
	height = float(raw_input("Enter the height of the triangle "))
	area = base * height / 2
	print_slow("Uni, Bi, Tri...\n")
	sleep(1)
	print_slow("Area: %.2f. \n%s \n" % (area, hint))
elif option[0] == "S":
	base = float(raw_input("Enter the base of the square or rectangle: "))
	height = float(raw_input("Enter the height of the square or rectangle: "))
	area = base * height
	print_slow("We're squaring up your answer...\n")
	sleep(1)
	print_slow("Area: %.2f. \n%s\n" % (area, hint))
elif option[0] == "R":
	diagonal_1 = float(raw_input("Enter diagonal 1 of the rhombus: "))
	diagonal_2 = float(raw_input("Enter diagonal 2 of the rhombus: "))
	area = diagonal_1 * diagonal_2 / 2
	print_slow("Pulling the rhombus into the station...\n")
	sleep(1)
	print_slow("Area: %.2f. \n%s\n" % (area, hint))
elif option[0:3] == "TRA":
	base_1 = float(raw_input("Enter the first base of the trapezoid: "))
	base_2 = float(raw_input("Enter the second base of the trapezoid: "))
	height = float(raw_input("Enter the height of the trapezoid: "))
	area = (base_1 + base_2) / 2 * height
	print_slow("Super-shape extrodinaire! Trapezoid! Trapezoid!\n")
	sleep(1)
	print_slow("... Uh, never mind ...\n")
	sleep(1)
	print_slow("Area: %.2f. \n%s\n" % (area, hint))
# and an else statement in case the user inputs garbage
else:
	print_slow("Error! Invalid shape specified. Exiting...\n")
	