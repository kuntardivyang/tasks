# Tuple Manipulations:
# Write a program that:
# Creates a tuple of numbers from 1 to 10.
# Finds the sum and product of all numbers in the tuple.

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print('Original Tuple : ', numbers)
print(f'Sum : {sum(numbers)}')
product = 1 
for i in numbers:
    product *= i
print(f'Product : {product}')