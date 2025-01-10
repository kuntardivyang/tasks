def reverse_string(word):
    return word[::-1]

def count_vowels(word):
    return sum(1 for x in word.lower() if x in 'aeiou')

def check_palindrome(word):
    return word == word[::-1]