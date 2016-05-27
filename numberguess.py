# A Simple Number Guessing Game 
#!/usr/bin/python

import random
import time

print("Welcome to the Simple Number Guess Game!")

def get_user_guess():
	user_guess = int(raw_input("Guess a number: "))
	return user_guess
	
def roll_dice(number_of_sides):
	first_roll = random.randint(1, number_of_sides)
	second_roll = random.randint(1, number_of_sides)
	max_val = number_of_sides * 2
	print("The maximum possible value is " + str(max_val))
	time.sleep(1)
	user_guess = get_user_guess()
	if user_guess > max_val:
		print("You did not enter a valid number. Exiting...")
		return
	else:
		print("Rolling..")
		time.sleep(2)
		print("Die 1: %d.") % (first_roll)
		print("Die 2: %d.") % (second_roll)
		time.sleep(1)
		total_roll = first_roll + second_roll
		print("Total dice: %d") % (total_roll)
		print("Result...")
		time.sleep(1)
		if user_guess > total_roll:
			print("Congratulations, you win!")
		else:
			print("Sorry, you have lost.")
			return
roll_dice(int(raw_input("Please enter the sides of a single die: ")))
