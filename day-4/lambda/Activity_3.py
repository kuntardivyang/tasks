# Use filter() and a lambda function to extract words longer than 4 characters from a list of strings.

def Activity_3():


    longer_list = filter(lambda a: len(a)>4,['RdFlex','car','bike','motor','bottle','Divyang'])

    print(list(longer_list))
    
Activity_3()