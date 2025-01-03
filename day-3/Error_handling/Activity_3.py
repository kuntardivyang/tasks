# Implement error handling in a function that takes user input, converts it to an integer, and divides a number by it.


def check_error():
    
    try:
        user_input1 = input('Enter Any Number One ')
        user_input2 = input('Enter Any Number Two ')
        
        num1, num2 = int(user_input1), int(user_input2)
        
        division = num1/num2
        
        print('Division : ', division)
    except ValueError as e:
        print(e)
        print('Enter Valid Inputs')
    except ZeroDivisionError as e:
        print(e)
        print('You can not divide Any value with zero')

check_error()
