# Week 8 - Problem Sheet
# Author - Brendan Heeney

# Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

import numpy as np                  # Importing Numpy

import matplotlib.pyplot as plt     # Importing Matplotlib - required to create the plot

x = np.arange(5)                    # numpy.arange(5) will give evenly spaced values up to but not including 5 with 1 as the default interval

f = x                               # Inserting the functions as provide
g = x*x
h = x*x*x 

plt.plot(f, label = "f=x", color = "green")                             # Plotting the functions using standard plt.plot functionality                        
plt.plot(g, label = "f=x^2", color = "red", linestyle = "dotted")       # Adding in labels for the legend
plt.plot(h, label = "f=x^3", color = "blue")                            # Choosing colors / styles

plt.title("Week 8 Problem Sheet - Three Functions")                     # Adding a Title
plt.xlabel("X Values")                                                  # Adding Labels to each Axis
plt.ylabel("Function Values")

plt.legend()                                                            # Adding a Legend
plt.grid()                                                              # Adding a Grid Effect

plt.savefig("Week_8_Task_Plot.png")                                     # Saving the Plot image

plt.show()                                                              # Display the Plot