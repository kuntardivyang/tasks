# Create a custom module with utility functions (factorial, is_prime, reverse_string) and use it in another script.
import custom
try :    
    user_input = int(input('Enter Number to print its factorial : '))
    fact = custom.factorial(user_input)
    print(f'Factorial of a number is : {fact} \n')

    user_input = int(input('Enter Number to check, is it prime or not : '))
    prime = custom.is_prime(user_input)
    print(f' Whether a given number Prime : {prime} \n')

    user_input = input('Type a string to reverse it : ')
    r_string = custom.reverse_string(user_input)
    print(f'Reversed String is : {r_string} \n')
except Exception as e:
    print(e)