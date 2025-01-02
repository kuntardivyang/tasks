#  Fifth Task

# - Create a program that:
#     - Accepts a string, a word to find, and a word to replace it with.
#     - Replaces all occurrences of the word and displays the modified string.
#     - Example: Input: `"I love Python. Python is great!"`, Replace `"Python"` with `"coding"`, Output: `"I love coding. coding is great!"`.

string=input("enter a string ")
word=input("A Word to find ")
repl=input("A word to replace ")
print(string.replace(word,repl))

