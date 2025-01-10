#Create a lambda function to check if a number is even or odd.

def Activity_1():

    even_or_odd = lambda a: a%2==0

    for i in range(1,101):
        if even_or_odd(i):
            print(i)

Activity_1()