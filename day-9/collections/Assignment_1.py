# Write a program to:
# Use Counter to analyze the frequency of words in a text file.
# Identify the top 5 most common words.
from collections import Counter
with open('file.txt','r') as file:
    freq = Counter(file.read().split())
    print('Frequency of words : ', freq)
    print('Top 5 common words are : ', freq.most_common(5))