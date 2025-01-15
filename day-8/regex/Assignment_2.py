# Write a program to:
# Extract all email addresses from a large text document.
# Replace sensitive information (like phone numbers) in a text file with ****.
import re

with open('large_text.txt', 'r') as file:
    text = file.read()

e_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(e_pattern, text)

p_pattern = r'\b\d{10}\b' 
new_text = re.sub(p_pattern, '****', text)

with open('file.txt', 'w') as file:
    file.write(new_text)

print("Emails : ", emails)