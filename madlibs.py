# A Mad Libs-like program.
# Author Hvitserk the Berserker

#!/usr/bin/python

print "Welcome to Mad Libs!"

main_char = raw_input("Enter a name: ")
adj_1 = raw_input("Enter an adjective: ")
adj_2 = raw_input("Enter a second adjective: ")
adj_3 = raw_input("Enter one more adjective: ")
verb_1 = raw_input("Enter a verb: ")
verb_2 = raw_input("Enter a second verb: ")
verb_3 = raw_input("Enter one more verb: ")
print "Now we will need four (4) nouns"
noun_1 = raw_input("Enter the first noun: ")
noun_2 = raw_input("Enter a second noun: ")
noun_3 = raw_input("Enter a third noun: ")
noun_4 = raw_input("Enter the last noun: ")
animal = raw_input("Enter an animal: ")
food = raw_input("Enter a food: ")
fruit = raw_input("Enter a fruit: ")
number = raw_input("Enter a number: ")
superhero = raw_input("Name a superhero: ")
country = raw_input("Name a country: ")
dessert = raw_input("Name a favorite dessert: ")
year = raw_input("Enter a year: ")


#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s.\nOn the other side of the %s were many %ss protesting to keep %s in stores.\nThe crowd began to %s to the rythym of the %s, which made all of the %ss very %s.\n%s tried to %s into the sewers and found %s rats.\nNeeding help, %s quickly called %s.\n%s appeared and saved %s by flying to %s and dropping %s into a puddle of %s.\n%s then fell asleep and woke up in the year %s, in a world where %ss ruled the world.\n"

print STORY % (adj_1, main_char, verb_1, adj_2, noun_1, noun_2, animal, food, verb_2, noun_3, fruit, adj_3, main_char, verb_3, number, main_char, superhero, superhero, main_char, country, main_char, dessert, main_char, year, noun_4)
