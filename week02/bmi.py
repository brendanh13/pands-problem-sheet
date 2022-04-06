# Week 2 - Weekly Task

# Create program to calculate body-mass index
# Inputs are height (cm) and weight (kg)

# Author: Brendan Heeney



weight = int(input("Enter your weight in kg:")) # First input is weight - we need to use int so we can display it with a string
print ("your weight is {}".format(weight))


height = int(input("Enter your height in cms:")) # Second input is height - again we use int
print ("your height is {}".format(height))

# We will convert the height in centimetres to height in metres before doing the calculation

mheight = height/100    # height in meters equals height in centimetres divided by 100


bmi = round((weight / (mheight*mheight)),2) # this is the calculation where i use to two inputs to work out BMI
                                            # additionally I have added rounding to 2 decimal places
print ("your bmi is {} kg/(m^2)".format(bmi))

# The BMI (Body Mass Index) in (kg/m2) is equal to the mass in kilograms (kg) divided by the square height in meters (m):

