# Combined Mini-Project:
# Build a program that:
# Reads a CSV file containing student names and scores (use a sample file or mock data).
# Calculates the average score and writes it back into a new file.
# Handles any file-related errors.

try:
    
    file = open('student-dataset.csv')
    file2 = open('new_data.csv','w')
    
except FileNotFoundError as e:
    print(e)

file2.write('name,science,maths,english,average\n')

try :
    x = file.readline()
    for i in file.readlines():
        data = i.split(',')

        name = data[1]
        science = int(data[2])
        maths = int(data[3])
        english = int(data[4])

        average = round((science + english + maths)/3, 2)

        file2.write(name + ',')
        file2.write(str(science) + ',')
        file2.write(str(maths) + ',')
        file2.write(str(english) + ',')
        file2.write(str(average) + '\n')
        
except IOError as e:
    print(e)       
    
    
file.close()
file2.close()