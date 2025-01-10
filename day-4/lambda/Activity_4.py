# Use reduce() to concatenate a list of strings into a single string.


def Activity_4():
    
    from functools import reduce

    combined_list = reduce(lambda a,b:a+b,['RdFlex','car','bike','motor','bottle','Divyang'])

    print(combined_list)
    
Activity_4()