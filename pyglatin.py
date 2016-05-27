# A Simple Pig Latin Translator

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
