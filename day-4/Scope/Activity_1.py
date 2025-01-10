# Write a program to illustrate how modifying a global variable inside a function affects its value.
variable = 10
print('Variable before function : ', variable)

def Activity_1():
    variable=5
    print('Variable inside a function : ', variable)
    
Activity_1()       
print('Variable after function : ', variable)