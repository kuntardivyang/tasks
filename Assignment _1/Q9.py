# Text Statistics:
# Write a program to calculate:
# Total number of words in a paragraph.
# Total number of sentences.
# Average word length.

paragraph="""
this is just a sample paragraph
today is my first day as intern
i really liked the vibe here
"""


print(paragraph)
total_words=len(paragraph.split())
total_characters=len([x for x in paragraph if x not in ' \n'])
print("Total number of words : ", total_words)
print("Total number of sentances : ", len(paragraph.strip().split('\n')))
print('Average word length ',total_characters//total_words)
