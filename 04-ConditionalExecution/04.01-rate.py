# PY4E 04-ConditionalExecution 04.01-rate.py

# Write a program to prompt the user for hours and rate per hour using input to 
# compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times 
# the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate 
# of 10.50 per hour to test the program .
# You should use input to read a string and float() to convert the string to a 
# number.
# Do not worry about error checking the user input - assume the user types 
# numbers properly.
# The output should be '498.75'

HOURS_BEFORE_OVERTIME = 40
OVERTIME_RATE = 1.5

'''Prompts'''
# get hours worked from user as float
hours = float(input("Please enter hours worked: "))
# get rate of pay from user as float
rate = float(input("Please enter rate of pay: "))

'''Calculations'''
# basic pay
pay = hours * rate
# overtime
if hours > HOURS_BEFORE_OVERTIME:
    pay = pay + (OVERTIME_RATE - 1) * ((hours - 40) * rate)

'''Output'''
# gross pay
print(pay)

