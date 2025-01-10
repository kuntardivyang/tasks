# Compare how variables behave inside a loop versus outside it using different scopes.

def Activity_4():
    
    variable = 1
    print('Outside a loop variable is : ', variable)
    for i in range(5):
        variable = i # Changing global scope variable
        print('Inside a loop variable is : ', variable)
    print('After a loop variable is : ', variable)

Activity_4()
