# Functions
# Write a function to calculate the factorial of a number.




# Activity 1
def factorial(x):
    result = 1
    for i in range(1,x+1):
        result *= i
    return result
print('Factorial : ', factorial(int(input('Enter A Number to calculate the factorial of it : '))))
     