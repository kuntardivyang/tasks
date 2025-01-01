# # Question 3 Basic String Manipulations:
# Write a program that:
#     Takes a sentence as input.   
#     Converts the sentence to uppercase and lowercase.
#     Removes all spaces and counts the total number of characters.



word=input("enter a sentence ")


print("Your input in uppercase ",word.upper())
print("Your input in lowercase ",word.lower())
print("Your input without spaces ",word.replace(' ', ''))
print("Total number of characters ",len(word.replace(' ', '')))