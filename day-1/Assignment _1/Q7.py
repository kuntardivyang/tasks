# Character Frequency Counter:
# Counts the frequency of each character (ignoring case) in a string.
# Outputs the result in a dictionary.
# Example: Input: "Hello", Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}.

string=input('Enter A String ').strip().lower()
char=dict()
for i in string:
    char[i]=0
for i in string:
    char[i]+=1
    
print(char)