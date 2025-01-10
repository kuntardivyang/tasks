def factorial(number):
    if number == 0 :
        return 1
    return number * factorial(number - 1)
    
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def reverse_string(word):
    return word[::-1]