# Write a program to:
# Count the frequency of characters in a string using Counter.
from collections import Counter

user_input = Counter(input('Enter A String : ').strip().replace(' ', ''))
print(f'Frequency of a counter in application : {user_input}')

# Find the top 3 most common elements in a list.
print(f'Most Common Elements : {user_input.most_common(3)}')