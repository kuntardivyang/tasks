# Write a program to:
# Read a text file and count the number of lines, words, and characters in it.
# Handle cases where the file does not exist using exception handling.
import logging

logging.basicConfig(filename='errors.log',
                    format='%(asctime)s %(message)s',
                    filemode='a')

logger = logging.getLogger()

def count(file_path):
    num_lines = 0
    num_words = 0
    num_chars = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            num_lines += 1
            num_words += len(line.split())
            num_chars += len(line.replace(' ', ''))
        
    return num_lines, num_words, num_chars

try:
    lines, words, chars = count('file.txt')
    print(f'Number of lines {lines}, Number of Words {words}, Number of chars {chars}')
except FileNotFoundError:
    logger.exception('File Not Found on specified path ')