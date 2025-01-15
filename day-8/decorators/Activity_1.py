# Write a program to:
# Create a decorator to log the execution time of a function.
import time
import logging
logging.basicConfig(filename='info.log',
                    format='%(asctime)s %(message)s',
                    filemode='a')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def function_time(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        logger.info(f'Execution time  {end_time - start_time} seconds')
        return result
    return wrapper

@function_time
def Activity_1():
    print("Activity_1 Part 1 executed.")

Activity_1()

# Create a decorator that checks user authentication before executing a function.
def check_authentication(func):
    def wrapper():
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()
        if username == "admin" and password == "password":
            print("User authenticated!")
            return func()
        else:
            print("Invalid username or password!")
            return None
    return wrapper

@check_authentication
def Activity_1():
    print("Activity_1 Part 2 executed.")

Activity_1()
