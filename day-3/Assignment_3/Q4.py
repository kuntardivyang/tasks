# Error Handling:
# Write a program that:
# Prompts the user for a number, divides 100 by it, and handles any errors.
# Ensures that the program does not crash for invalid inputs and always prints "Program Completed" at the end.


try:
    user_input = int(input('Type A Number '))
    division = user_input/100
    print(division)
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)
finally:
    print('Program Completed')