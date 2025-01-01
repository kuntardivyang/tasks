# String Reversal with Conditions:
#     Reverses the order of words in a sentence.
#     Example: "Hello World" → "World Hello".
#     If the sentence contains less than three words, return the string unchanged.


string=input('Enter a string : ')
words=string.split(' ')
result=''
if len(words)>3:
    for i in words:
        result=i+" "+result
    print(result)
else:
    print(string)