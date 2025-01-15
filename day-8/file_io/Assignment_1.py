# Write a program to:
# Accept a file path from the user and count the frequency of each word in the file.
# Write the word frequencies into a new text file.
def count_words(file_path):
    word_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()
                word_count[word] = word_count.get(word, 0) + 1
    return word_count

def write_words(word_count, output_file_path):
    with open(output_file_path, 'w') as file:
        for word, count in sorted(word_count.items()):
            file.write(f"{word}: {count}\n")

input_path = input("Enter the file path (e.g.  ./file.txt  ): ")
output_path = "word_count.txt"

word_count = count_words(input_path)
write_words(word_count, output_path)