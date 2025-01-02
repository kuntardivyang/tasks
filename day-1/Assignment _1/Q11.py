# Vowel and Consonant Counter:
#     Write a program that:
#         Counts the number of vowels and consonants in a string.
#         Outputs the result in a dictionary.
#         Example: Input: "Hello World", Output: {'vowels': 3, 'consonants': 7}.



# string='Hello this is Harry Potter'
string=input('Enter A String : ')

resultant={'vowels':0,'consonant':0}
vowel_string='aeiou'
for i in string.lower().replace(' ', ''):
    if i in vowel_string:
        resultant['vowels']+=1
    else:
        resultant['consonant']+=1
print(resultant)
        