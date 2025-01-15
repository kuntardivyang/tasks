# Create a program that:
# Uses defaultdict to group words by their lengths from a list of strings.
# Handles cases where a word length does not exist.
from collections import defaultdict 

d = defaultdict(int)
user_input = input('Enter A String : ').strip().split()
for i in user_input:
    d[i] += 1
print(d)