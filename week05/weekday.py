# Problem Sheet for Week 5

# Author: Brendan Heeney

# Write a program that outputs whether or not today is a weekday.



from datetime import datetime

dayOfWeek = datetime.today().weekday()   # found on internet - this tells us which day of the week today is; 0 = Mon, 1 = Tue etc

daysOfWeek = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")  # not now required for this exercise

#weekDays = daysOfWeek[0:5]

#print(weekDays)
#print(dayOfWeek)  # told me today = 5 which is Saturday (as I write this on a Saturday!)


if dayOfWeek < 5:     # this will be a number from 0 - 6 depending on which day of the week it is
    print("Yes, unfortunately today is a weekday.")
else:
    print ("It is the weekend, yay!")
    
