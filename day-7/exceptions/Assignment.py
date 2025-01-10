# Write a program that:
# Prompts the user to input two numbers and divides them.
# Handles ZeroDivisionError, ValueError, and logs any unhandled exceptions to a file.
# Creates a custom exception InvalidAgeError and raises it if a user enters an age less than 0 or greater than 100.
import logging

logging.basicConfig(filename="errors.log", 
                    format='%(asctime)s %(message)s',
                    filemode='a+')

logger = logging.getLogger()

class InvalidAgeError(Exception):
    """Exception raised for Invalid User Input for age ."""
    def __init__(self, message):
        super().__init__(message)
        
try: 
    num1 = int(input('Enter First Number : '))
    num2 = int(input('Enter Second Number : '))
    print('Division of given numbers is : ', num1 / num2)
except ValueError as e:
    print(e)
    logger.error(e)
except ZeroDivisionError as e:
    print(e)
    logger.error(e)
except Exception as e: 
    logger.error(e)

Age = int(input('Enter A Age : '))    
if(Age > 100 or Age < 0):
    raise InvalidAgeError('Age must be in range 0 to 100')
