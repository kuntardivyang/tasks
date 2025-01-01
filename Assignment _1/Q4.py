# 
# 
# Word Count Program:
#
# Accepts a multi-line string.
# Splits it into words.
# Counts the frequency of each word.
# Outputs the result in a dictionary.

freq_words=dict()


multi_line=input('Enter multi line string')
words=multi_line.strip().split(' ')

for i in words:
    freq_words[i]=0
for i in words:
    freq_words[i]+=1
    
print(freq_words)