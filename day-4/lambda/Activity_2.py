# Use map() with a lambda function to add 10 to each element in a list.

def Activity_2():
    num_list = range(1,11)
    
    add_10 = lambda a:a+10
    
    
    num_list = map(add_10,num_list)
    
    print('10 Added List : ', list(num_list))
    

Activity_2()