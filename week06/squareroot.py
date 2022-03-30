# Problem Sheet for Week 6

# Author: Brendan Heeney

# Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
# You should create a function called <tt>sqrt</tt> that does this.
# I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).
# This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods).
# I suggest that you look at the newton method at estimating square roots.



def sqrt(x):                   # defining the function called sqrt which we want to give us the square root of x
    z=x                        
    for i in range(100):       # the idea behind this is that with Newtons Method; we need to keep iterating to try to get closer to the correct square root so we are setting a limit of 100 iternations
        x = 0.5*(x+(z/x))      # this is the formula as per the research of Newtons Method
    return x                   # this returns the approximation of the last iteration

a = int(input("Enter any postive integer: ")) # ask for number to be input
print("The square root is {}".format(sqrt(a))) # this prints the value - using the format option to ouptput the numerical value beside the



