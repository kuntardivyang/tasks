# Write a package for basic string utilities like reversing strings, counting vowels, and checking palindromes.
# 	string_utils/
# 	    ├── __init__.py
# 	    ├── operations.py
import string_utils

word = input('Enter A String : ')

print('The reverse of given word is ', string_utils.reverse_string(word))
print('No. of vowels in given string is ', string_utils.count_vowels(word))
print('Whether a given string is palindrome ', string_utils.check_palindrome(word))