# Write a program that:
# Creates a @retry decorator to retry a function if it raises an exception.
# Logs every function call (with its arguments and return value) using a decorator.
# Develop a program to:
# Create a @singleton decorator that ensures only one instance of a class can be created.
# Use a decorator to memoize the results of a recursive function (e.g., Fibo
import time
import logging

logging.basicConfig(filename='errors.log',
                    format='%(asctime)s %(message)s',
                    level = logging.DEBUG,
                    filemode='a')

logger = logging.getLogger()

def retry(max_retries, wait_time):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    retries += 1
                    logger.error(f'No. of retries {retries} of function {func.__name__}')
                    time.sleep(wait_time)
            logger.exception("function exceeds maximum attempts. ")
        return wrapper
    return decorator

def make_logs(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f"Called this func : {func.__name__}")
        return result
    return wrapper

@retry(max_retries = 3, wait_time = 1)
@make_logs
def Q1():
    x = 'Divyang' 
    if isinstance(x, str):
        raise ValueError('Testing Retry Decorator')

def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        print(cache)
        print(cache[args]) 
        logger.info(f'Hello Memoize : {cache}')
        return result

    return wrapper

@make_logs
@singleton
class Test:
    def __init__(self, name):
        self.name = name

@make_logs
@memoize
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

Q1()
    
obj1 = Test('Divyang')
obj2 = Test('Smit')

print('First Object variable name : ', obj1.name)
print('Second Object variable name : ', obj2.name)
print(factorial(int(input('Enter Number to find its factorial. '))))  