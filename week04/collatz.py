# Week 4 - Weekly Task

# Write a program that asks the user to input any 
# positive integer and outputs the successive values of the following calculation:

# At each step calculate the next value by taking the 
# current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.

# Author = Brendan Heeney



n = int(input("Please enter a positive integer: "))

while n != 1:                   # we know that we exit when the number is 1 so we set our number to be not equal to 1
    if n % 2 == 0:              # we check if the number is even
        n = n / 2               # if it is true; we divide it by 2
    else:
        n = 3 * n + 1           # else we multiply by 3 and add 1
    print(int(n), end=" ")      # the int makes sure we return integers only with no decimal places - as per task
                                # the end=" " allows us to keep the output on one line
      
