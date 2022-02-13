# Week 2 - Weekly Task
# Create program to calculate body-mass index
# inputs are height (cm) and weight (kg)
# Author: Brendan Heeney


# First input is weight - we need to use int so we can display it with a string
weight = int(input("Enter your weight in kg:"))
print ("your weight is {}".format(weight))

# Second input is height - again we use int
height = int(input("Enter your height in cms:"))
print ("your height is {}".format(height))

# We will convert the height in centimetres to height in metres before doing the calculation

mheight = height/100


bmi = weight / (mheight*mheight)
print ("your bmi is {}".format(bmi))

# The BMI (Body Mass Index) in (kg/m2) is equal to the mass in kilograms (kg) divided by the square height in meters (m):

