# Extract even numbers from a list and their squares in a dictionary using comprehensions.


square_dict = { i:i**2 for i in range(1, 11) if i%2==0 }

print(square_dict)
