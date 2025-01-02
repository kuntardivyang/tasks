#Assignment 1


### First
# Write a program that asks for a user's full name and performs the following:
# Prints the initials.
# Reverses the name.
# Checks if the name is a palindrome.

fullName=input("Enter Your FullName : ")

fullName=fullName.strip().split(' ')

print('Full Name is ',fullName)

print('Initials ',fullName[0][0]+fullName[1][0])
print('Name in reverse format : ',fullName[0][::-1])
print()

name=fullName[1]

if name==name[::-1]:
    print('the name is palindrome')
else:
    print('Name is not palindrome')
    
    
