# Functions
# Write a lambda function to filter even numbers from a list.

 




# Activity 3
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
even_list = filter(lambda x: x % 2 == 0, number_list)
print('Even List : ', list(even_list))