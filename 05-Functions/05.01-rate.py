# PY4E 05-Functions 05.01-rate.py

# Write a program to prompt the user for hours and rate per hour using input to 
# compute gross pay. Pay should be the normal rate for hours up to 40 and 
# time-and-a-half for the hourly rate for all hours worked above 40 hours. Put 
# the logic to do the computation of pay in a function called computePay() and 
# use the function to do the computation. The function should return a value. 
# Use 45 hours and a rate of 10.50 per hour to test the program 
# You should use input to read a string and float() to convert the string to a 
# number.
# Do not worry about error checking the user input unless you want to - you can 
# assume the user types numbers properly. 
# Do not name your variable sum or use the sum() function.
# The output should be 'Pay 498.75'

'''Constants'''
HOURS_BEFORE_OVERTIME = 40
OVERTIME_BONUS = 0.5

'''Function'''
def computePay(hours, rate):
    """calculates gross pay

    Args:
        hours (float): number of hours worked
        rate (float): pay per hour

    Returns:
        float: gross pay including overtime
    """
    pay = hours * rate
    if hours > HOURS_BEFORE_OVERTIME:
        pay += OVERTIME_BONUS * (hours - 40) * rate
    return pay

'''Prompts'''
hours = float(input("Please enter hours worked: "))
rate = float(input("Please enter rate of pay: "))

'''Output'''
print("Pay", computePay(hours, rate))