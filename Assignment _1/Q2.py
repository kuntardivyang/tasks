
    
### Second

# Question 2 Create a function to count the number of each vowel in a given string.

def count_each_vowel():
    vowel=dict()
    word=input('Enter Your String whose vowels you want to count ').lower()
    vowels='aeiou'
    for i in word:
        if i in vowels:
            vowel[i]=1

    for i in word:
        if i in vowels:
            vowel[i]=vowel[i]+1
    print(vowel)
    