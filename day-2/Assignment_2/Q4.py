# Set Operations:
# Write a program that:
# Accepts two lists of numbers.
# Converts them to sets and finds their union, intersection, and difference.


print()


list_one = input('Enter First List of Number ( e.g  1 2 3 4 5  ) ').strip().split(' ')
list_two = input('Enter Second List of Number ( e.g  1 2 3 4 5  ) ').strip().split(' ')

for i in range(len(list_one)):
    list_one[i] = int(list_one[i])
    
for i in range(len(list_two)):
    list_two[i] = int(list_two[i])


set_one = set(list_one)
set_two = set(list_two)


print(f' Set one : {set_one}')
print(f' Set two : {set_two}')

print(f' Union {set_one.union(set_two)}')
print(f' intersection {set_one.intersection(set_two)}')
print(f' differnce of set one from set two {set_one.difference(set_two)}')

