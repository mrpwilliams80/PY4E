# 03 VariablesExpressionsStatements 0301-rate.py

# autograder: prompt user for hours and rate per hour using input and compute 
# gross pay. use 35 hours and a rate of 2.75 per hour to test the program 
# (the pay should be 96.25).
# use input to read a string and float() to convert the string to a number.
# Do not worry about error checking or bad user data.

hours = float(input("Enter hours worked: "))
rate = float(input("Enter rate of pay per hour: "))
print("Your gross pay is:", hours * rate)