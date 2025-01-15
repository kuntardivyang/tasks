# Create a program to:
# Replace all occurrences of a word in a text file with another word.
# Find all dates in the format dd-mm-yyyy or yyyy-mm-dd in a given string.
import re

sentence = input('Type a Sentence ')
target = input('type the target word you want to replace : ')
replace_word = input('type the replace word ')
print(re.sub(target, replace_word, sentence)) 

user_input = input('Type string that has dates : ')
dates = re.findall(r'\b(\d{2}-\d{2}-\d{4}|\d{4}-\d{2}-\d{2})\b',user_input)
print(dates)