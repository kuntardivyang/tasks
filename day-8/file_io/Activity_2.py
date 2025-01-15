# Create a program to:
# Write a list of numbers to a text file.
# Read the file back and calculate their sum.
with open('file2.txt','w+') as file:
    file.write(' '.join(map(str,list(range(1,11)))))
    file.seek(0)
    total = sum(map(int,file.read().split()))
    print(f'Total Sum : {total}')