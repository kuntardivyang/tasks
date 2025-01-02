# Write programs using list methods:

#     Find the second largest number in a list.


def activity_two():
    
    list = [5, 62, 46, 74, 124, 6, 7, 4, 3, 2, 1]
    list.sort(reverse=True)
    print('Second Largest Number : ', list[1])

activity_two()