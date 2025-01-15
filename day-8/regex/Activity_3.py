# Use regular expressions to:
# Identify and extract hashtags from a social media post.
# Validate passwords (e.g., length >= 8, at least one uppercase letter, one digit, and one special character).
import re
caption = input('Type your insta caption with hashtags : ')
hashtags = re.findall(r'#\w+',caption)
print(hashtags)

password = input('Type a password: ')
pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$'

if re.match(pattern, password):
    print('Password is valid')
else:
    print('Password is invalid')