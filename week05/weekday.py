# Week 5 - Weekly Task

# Write a program that outputs whether or not today is a weekday.

# Author: Brendan Heeney

from datetime import datetime

dayOfWeek = datetime.today().weekday()   # this tells us which day of the week today is; 0 = Mon, 1 = Tue etc

if dayOfWeek < 5:     # this will be a number from 0 - 6 depending on which day of the week it is
    print("Yes, unfortunately today is a weekday.")
else:
    print ("It is the weekend, yay!")
    
