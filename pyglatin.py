#################################################################
#				 A Simple Pig Latin Translator 					#
#																#
# This very simple Python app will take text input into it and 	#
# and either reject it for not following the rules of Pig Latin #
# or it will work as intended & take the first letter of a word	#
#	and place it at the end with the suffix "ay" added to it	#
#							Have fun!							#
#																#
#  This program and its source are 100% libre. You are FREE to 	#
# run, study, share (copy), and modify this software so long as #
# 		these rights are retained in future incarnations. 		#
#						  Happy coding!							#
#																#
# Author: Hvitserk the Berserker & CodeCademy	  Copyleft 2016	#
#################################################################
#!/usr/bin/python

print "Welcome to the Pig Latin Translator!"

name = raw_input("What is your name? ")
print "Hello, %s!" % (name)

pyg = "ay"

original = raw_input("Please enter a word: ")

"""
An if statement to verify the entered string has letters only
and to take that word and concatenate it to the new output
"""
if len(original) > 0 and original.isalpha():
	word = original.lower()
	first = word[0]
	new_word = word + first + pyg
	new_word = new_word[1:len(new_word)]
	print new_word
else:
	print "You did not enter a word."