# pands-problem-sheet
# PandS 2022 Weekly Tasks
# Author: Brendan Heeney

# This readme file provides additional details for each of the weekly tasks for the 2022 Programming and Scripting Module

# Week 2

Write a program that calculates somebody's Body Mass Index (BMI). Call the file bmi.py
        - The inputs are the person's height in centimetres and weight in kilograms.
        - The output their BMI (You may need to look up how this is calculated)

1 - Confirmed the formula to calculate the BMI as weight in kg divided by height in meters squared

        Formula: weight (kg) / [height (m)]2

Reference 2.1: https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_1.html

2 - Inputs - I have used 'int' as part of the input variables as we need them to be in number format for later calculations

3 - Convert Height - Basic divide by 100 to convert height in cm to height in metres

4 - Calculation with Rounding - calculation is completed as per the formula.  Have also added rounding to two decimal places - as noted in the task.

Reference 2.2: https://www.w3schools.com/python/ref_func_round.asp


# Week 3

Write a program that asks a user to input a string and outputs every second letter in reverse order.

1 - This is strings so further research completed on Strings

Reference 3.1: https://www.w3schools.com/python/python_strings.asp

2 - We need to ask for a string so we start by asking the user to type in a string via input

variable = input("text")

3 - We know we need to do a variety of actions to the string so I am calling the initial string as rawString
    When we have the string - we are asked to do the following:
    i)  Output every second letter
    ii) Reverse the order

    Both of these concepts were explained below:
        Skipping ->
                string = "welcome to freecodecamp"
                print(string[::2])

        Reversing ->
                string = "welcome to freecodecamp"
                print(string[::-1])

Reference 3.2: https://www.freecodecamp.org/news/python-substring-how-to-slice-a-string/

4 - Applying both of the concepts in 3 above; I am able to print out the desired format       

# Week 4

Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation:
At each step calculate the next value by taking the current value and, if it is even, divide it by 2, but if it is odd, multiply it by 3 and add 1.
Have the program end if the current value is 1.

1 - We have been directed to the Collatz Conjecture as reseach for this task.  Initial research focus on Youtube video link provided in Moodle Notes

Reference 4.1 https://www.youtube.com/watch?v=094y1Z2wpJg&t=1s

2 - Have also found the collatz sequence described below:

Reference 4.2: https://www.geeksforgeeks.org/collatz-sequence/

Starting with any positive integer N, we define the Collatz sequence corresponding to N as the numbers formed by the following operations:

N → N/2 ( if N is even)
N → 3N + 1 (if N is odd)

i.e. If N is even, divide it by 2 to get N/2. 
If N is odd, multiply it by 3 and add 1 to obtain 3N + 1.

3 - We now need to put this into a WHILE loop (we use a while statement because we dont know how many iterations of the loop we will need to get to the end)

Initially reviewed the basics of WHILE loops in W3Schools followed by applying a WHILE loop to the collatz sequence for Python

Reference 4.3: https://www.w3schools.com/python/python_while_loops.asp

Reference 4.4: https://www.geeksforgeeks.org/program-to-print-collatz-sequence/

4 - Going about building it
        a.      We ask for the input of a number
        b.      We implement the WHILE loop with an ELSE condition
                        Starting with our input number not being equal to the exit condition we have been provided of the number 1; we use the IF portion to check if the number is
                        Even and then the ELSE portion to handle the odd numbers.
        c.      We add the calculation to each part - IF and ELSE
        d.      Print the numbers to the list
        e.      Until we reach a value of 1 when the code will not run any longer. (If output is != 1; the code continues to run...i.e restarts again)

5 - The desired numbers are printed - I have added in an end=" " which keeps the list on the same line.

Reference 4.5: https://www.tutorialspoint.com/how-to-print-in-same-line-in-python

# Week 5

Write a program that outputs whether or not today is a weekday.

An example of running this program on a Thursday is given below.

$ python weekday.py
Yes, unfortunately today is a weekday.

1 - Firstly - we need to find out a method of figuring out the days of week in Python

I researched a turtorial at below page which helped me understand this.

To work out which day it is - we need to import a datetime module

Sample: from datetime import datetime

Reference 5.1: https://www.delftstack.com/howto/python/python-datetime-day-of-week/

Once I was able to work out what any given day is - I can then use this in my program

0 = Mon, 1 = Tue etc

2 - Once I have the day of the week as a number, I just need to do a simple IF / ELSE statement to print what I want

# Week 6

1 - Research the Newton's Method of Square Roots

Reference 6.1: https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf -> theory behind it with formulae

Reference 6.2: https://en.wikipedia.org/wiki/Newton%27s_method#Square_root -> this is a nice worked example of the square root of 612

Reference 6.3: https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo -> good explanation

2 - To summarize what Netwon's Method is; assume an approximate value as the sqaure root - try to find a better value until the better value becomes the actual square root value (or very close to it)

3 - In the squareroot.py file; we can see the following:
    i)      Defining the function which has one argument / input
    ii)     Given my understanding of the method - I know that I need to do a recursive action so we can get to (or close to) the sqaure root.
            I have chosen to use a for loop and run it 100 times to get the best approximation
    iii)    There are alternatives to the for loop - we could add some sort of precision / tolerance within the function to check if the approximate value changes after each 
            iteration are so small that there is no need to do any more iterations as we have arrived at the desired answer
            This tolerance level could be passed in as an argument in the function or we could define it in the function itself
    iv)     The formula I have written shows 0.5*XXX however it could also be written as XXX/2



# Week 7


# Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.
# The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.

1 - I found about Python and Command Line functionality

Reference 7.1: https://realpython.com/python-command-line-arguments/

=> Learning outcome here is that I can run Python commands from the Shell (Comman Line Interface)

Example:

$ python -c "print('Real Python')"
Real Python

2 - For the task; first thing I want to find out is how to read in a file into a program from a command line argument. 

Reference 7.2: https://www.tutorialspoint.com/python3/python_command_line_arguments.htm

Reference 7.3: https://www.tutorialspoint.com/How-to-read-a-file-from-command-line-using-Python

Above references explain the sys.argv concept and how it is used with the sys module of Python

--The Python sys module provides access to any command-line arguments via the sys.argv. This serves two purposes −
--sys.argv is the list of command-line arguments.
--len(sys.argv) is the number of command-line arguments.

Great Example provided;

Example
Consider the following script test.py −

#!/usr/bin/python3

import sys

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
Now run the above script as follows −

$ python test.py arg1 arg2 arg3
This produces the following result −

Number of arguments: 4 arguments.
Argument List: ['test.py', 'arg1', 'arg2', 'arg3']

NOTE − As mentioned above, the first argument is always the script name and it is also being counted in number of arguments.


3 - Now we need a method to find the number of e's in the file

For this I researched the count() function - I will use this to count the number of e's in the file

Refernce 7.4: https://www.w3schools.com/python/ref_list_count.asp






# Week 8

# Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

1 -     To start, I know I need to create a plot with 3 separate functions displayed on the one set of axes - with a range going from 0 - 4 on the X Axis (Horizontal)
        The functions are:
                f(x) = x
                g(x) = x^2
                h(x) = x^3

2 -     To confirm how to define the range from 0 - 4; I found the numpy.arange command

Reference 8.1           https://numpy.org/doc/stable/reference/generated/numpy.arange.html

3 -     Writing the functions is straightforward; I have done x^2 as x*x however this can also be written as x**2

4 -     I have then plotted the functions individually as learned in lecture
        Adding in additional features at this point to enhance the plot
        e.g colors and dotted lines

Reference 8.2           https://www.w3schools.com/python/matplotlib_line.asp

5 -     To further improve the plot; I am adding Titles and Labels

Reference 8.3           https://www.w3schools.com/python/matplotlib_labels.asp



