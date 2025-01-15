# Write a program to:
# Validate email addresses using regular expressions.
# Extract all phone numbers from a given text.
import re
pattern = r'\b[A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

user_input = input('Enter Your Email : ')
if re.fullmatch(pattern, user_input):
    print('Given email is valid')
else:
    print('Entered email is not valid')
    
user_input = input('Type string that has phone numbers : ')
phone_numbers = re.findall(r'[0-9]{10}',user_input)
print(phone_numbers)