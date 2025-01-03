# Write a program to handle a ZeroDivisionError gracefully.
# #

try:
    division = 1/0 
except ZeroDivisionError as e:
    print(e)
    print('You can not divide Any value with zero')
    