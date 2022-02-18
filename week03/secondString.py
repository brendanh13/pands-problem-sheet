# This is Week 3 Problem Sheet

# The task is to write a program that asks a user to input a string 
# and then outputs every second letter in reverse order

# Author: Brendan Heeney

rawString = input("Please enter a sentence: ") # ask for input of the initial string
skipString = rawString[::2] # skip every second letter in the string
reversedString = skipString[::-1] 

print(reversedString)