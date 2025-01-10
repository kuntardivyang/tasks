# Write a program to:
# Define a global counter and modify it inside a function using the global keyword.
# Demonstrate the behavior of nonlocal by creating a nested function that manipulates a variable in the enclosing scope.
# Write a function to check the visibility of a variable defined inside a loop.
counter = 0
class Scope:
    
    def Q1(self):
        print('Question 1 ↓ \n')
        global counter
        counter = 1
        print('Counter in function : ', counter)
        print()
        
    def Q2(self):
        print('Question 2 ↓ \n')
        counter = 0
        print('Counter inside a Outer function : ', counter)
        def nested_func():
            nonlocal counter
            counter = 1
            print('counter inside a nested function : ', counter)
        nested_func()
        print('Counter after executing nested function : ', counter)
        print()
    
    def Q3(self):
        print('Question 3 ↓ \n')     
        x = 1
        print('x before for loop ' , x)
        for i in range(3):
            x=i
            print('x inside for loop ' , x)
        print('x after for loop ' , x)
  
scope1=Scope()
scope1.Q1()
scope1.Q2()
scope1.Q3()