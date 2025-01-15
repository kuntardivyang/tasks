# Develop a program that:
# Uses a decorator to validate input arguments of a function.
import logging
from .Activity_1 import function_time
logging.basicConfig(filename='errors.log',
                    format='%(asctime)s %(message)s',
                    filemode='a')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def decorator(func):
    def wrapper(x, y):
        if isinstance(x, int) and isinstance(y, int):
            return func(x, y)
        else:
            print("inputs are not valid")
            return None
    return wrapper

# Chains multiple decorators to add both logging and validation to a function.
@function_time
@decorator
def add_numbers(x, y):
    return x + y

result = add_numbers(5, '10')  
print(result)  

result = add_numbers(5, 10) 
print(result)  
