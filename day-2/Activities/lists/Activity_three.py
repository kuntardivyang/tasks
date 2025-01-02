# Write programs using list methods:
#     Combine two lists and remove duplicates.
    
def activity_three():
    
    list_one = [1, 2, 3, 4, 5]
    list_two = [3, 4, 5, 6, 7]
    list_one.extend(list_two)
    print(list(set(list_one)))  #removing duplicates using set
    
    
activity_three()
