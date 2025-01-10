# Write a program that raises a ValueError if the user enters invalid input (e.g., entering a string when a number is expected).
# Use the logging module to log exceptions to a file instead of printing them to the console.
import logging

logging.basicConfig(filename="errors.log", 
                    format='%(asctime)s %(message)s',
                    filemode='a+')

logger = logging.getLogger()

try :
    number = int(input('Enter A Number '))
except ValueError as e:
    logger.error(e)