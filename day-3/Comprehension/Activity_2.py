# Create a dictionary of numbers and their squares using dictionary comprehensions.


num_dictionary = dict()  #Initialization

num_dictionary = { x:x**2 for x in range(1, 11) }

print(num_dictionary)