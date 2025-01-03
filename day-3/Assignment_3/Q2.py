# Dictionary Comprehensions:
# Write a program to:
# Create a dictionary from a list of words where keys are words and values are their lengths.
# Filter a dictionary to keep only items where the value is greater than 5.

words_list='If you are waiting for the right time its now believe you can and you are halfway there '.split()
words_dict=dict()

for i in words_list:
    words_dict[i]=len(i)
    
print('↓ Original Dictionary ↓')
print(words_dict)

filter_dict={x:y for x,y in words_dict.items() if y>5}

print('↓ filtered Dictionary ↓')
print(filter_dict)
