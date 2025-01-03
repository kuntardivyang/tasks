# Write a program to read a text file and count the frequency of each word.



# file Using with open()
with open('test.txt', 'r') as file:
    content = file.read()
    print(content)
    file.close()

# Using open()
file = open('test.txt')
# print(file.read())

words_list = [i for x in file.readlines() for i in x.split()]
file.close()

print('Words List : ', words_list)

freq_words=dict()

for i in words_list:
    freq_words[i] = freq_words.setdefault(i, 0) + 1
    
print('frequency of each word :', freq_words)

