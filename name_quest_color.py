#!/usr/bin/python
from datetime import datetime
name = raw_input("What is your name? ")
quest = raw_input("What is your quest? ")
color = raw_input("What is your favorite color? ")
now = datetime.now()

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)
print "By the way the date is %s/%s/%s and the current time is %s:%s:%s." % (now.month, now.day, now.year, now.hour, now.minute, now.second)