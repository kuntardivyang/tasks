# Write programs to:
# Merge two dictionaries.


def activity_2():
    
    ## By updating the first dictionary
    dict_one = dict({1:'One', 2:'Two', 3:'Three'})
    dict_two = dict({4:'Four', 5:'Five'})
    dict_one.update(dict_two)
    print('Activity 2 :')
    print(dict_one)
   
activity_2()