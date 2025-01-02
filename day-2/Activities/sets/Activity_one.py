# Sets
# Write programs to:
# Find unique elements from two lists using sets.


def activity_1():
    list_one = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 7,]
    list_two = [7, 8, 9, 10, 11, 1, 2, 3, 4, 5]
    unique = set(list_one + list_two)
    print(unique)
    
    
activity_1()