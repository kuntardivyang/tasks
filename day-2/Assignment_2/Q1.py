# List Operations:
# Write a program that:
# Accepts a list of integers.
# Returns a new list with duplicates removed, sorted in ascending order.


print('Enter List of integers separeted by space ( e.g 1 2 3 4 5 6 )')


integer_list = input().strip().split()

for i in range(len(integer_list)):
    integer_list[i] = int(integer_list[i])
    
print(f'Original List : {integer_list}')

# To remove duplicates we have used set approach

integer_list = list(set(integer_list))   #Duplicates Removed
print('Duplicates Removed : ', integer_list)
integer_list.sort()
print(f'Sorted List {integer_list}')