# Write a program that:
# Imports the datetime module to display the current date and time.
# Write a Python Program to get the current date and also month,year and day.
# How can you handle Timezones in python? Make one Example of it.
# Uses the math module to calculate the square root of a user-provided number.if the user enters invalid input then raise ValueError.
from datetime import datetime
import pytz
import math

date = datetime.now()
print('Date And Time : ', date)

print('Todays Date : ', date.strftime('%d'))
print('Month : ', date.strftime('%B'))
print('Year : ', date.strftime('%Y'))
print('Day : ', date.strftime('%A'))

print(f'date and time according to UTC {datetime.now(pytz.utc)}')
print(f'date and time according to Asia/Kolkata timezone {datetime.now(pytz.timezone('Asia/Kolkata'))}')
print(f'date and time according to America/NewYork timezone {datetime.now(pytz.timezone('America/New_York'))}')
print(f'date and time according to Europe/London timezone {datetime.now(pytz.timezone('Europe/London'))}')

try:
    number = int(input('Enter A Number to find its square root : '))
except ValueError: 
    raise ValueError('Input is not in valid format')

print('The Square root of given number is : ', round(math.sqrt(number), 2))