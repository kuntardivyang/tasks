# File Handling:
# Write a program to:
# Accept a list of names from the user and write them into a file.
# Read the file back and print the names in alphabetical order.


names_list=input('Type List of names separeted by spaces e.g divyang vishvam malav \n ').strip().split()

file=open('names.txt','w')
for name in names_list:
    file.write(name+'\n')    
file.close()


print('\n ↓ Names List ↓ ')
print(names_list)

names_list=open('names.txt','r').read().split()
names_list.sort()

print('\n ↓ Sorted Names List ↓ ')
print(names_list)


