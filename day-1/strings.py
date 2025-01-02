


#String Manipulations Exercises


###  1.  Reverse A String 


word="Hello How Are You"
result=''
for i in word:
    result=i+result
print(result)

###  2. Counting Vowels in a string

word="Hello how are you?"
vowels="aeiou"
word=word.lower()
count=0
for i in word:
    if i in vowels:
        count+=1
print("Vowels in string",count)


###  3. Replacing all spaces in a sentence with underscores.

word="I am Fine "
print(word.replace(' ', '_'))
