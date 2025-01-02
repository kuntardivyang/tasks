# Dictionary Operations:
# Write a program to:
# Count occurrences of each character in a given string using a dictionary.
# Delete a specific key from the dictionary and handle the case where the key does not exist.



word = 'Hello how are you'.lower()
occurences = dict()
for i in word.replace(' ', ''):
    if occurences.get(i):  
        occurences[i] += 1
    else: 
        occurences[i] = 1  
        
print('Counting occurrences of each character in a string and printing that dictionary.')
print(occurences)

print()

delete_key = input('Now enter the specific key you want to delete : ')

try :
    print(f'The deleted key is {delete_key} and its value is {occurences.pop(delete_key)}')
except KeyError:
    print('Provided Key doesnt exist')  