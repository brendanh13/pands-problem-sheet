# Week 7 Problem Sheet
# Author: Brendan Heeney

# Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.
# The program should take the filename from an argument on the command line. 


import sys              # need to import the sys module as per the readme file

with open(sys.argv[1], 'r') as f:    # this is standard code to read in a file that is passed as an argument
    contents = f.read()                # sys.argv[1] is the file ( sys.argv[0] is the first argument and is always the script name and it is also being counted in number of arguments.)                                         # f.read() will read the full file into the program

def letterFrequency(f, letter):         # we need a function that returns the number of e's in the file
    return contents.count(letter)       # here we are passing the filename and the letter into the function
                                        # and asking it to return the number of times the letter appears in the file using count()
letter = 'e'

print(letterFrequency(f, letter))      # displays the count of the number of the chosen letter (in this case e) from the file read in in the argument of the function