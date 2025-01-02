# Sets
# Write programs to:
# Use set comprehensions to generate squares of even numbers from 1 to 20.

def activity_3():
    squares = {x**2 for x in range(1, 20) if x%2 == 0}
    print('Squares of even numbers from 1 to 20.')
    print(squares)

activity_3()