# Write a program to read a file line by line and store non-empty lines in a list.

lines = []
with open('test_3.txt', 'r') as file:
    
    total_lines = len(file.readlines())
    file.seek(0)
    
    for i in range(total_lines):
        line = file.readline().strip()
        print(line)
        if line.strip():
            lines.append(line.strip())
            

    
print('Lines of file')
print(lines)