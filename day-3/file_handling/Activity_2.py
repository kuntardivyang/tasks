# Create a program to write user input into a file and read it back.

with open('test_2.txt', 'w') as file:
    flag = True
    while flag:
      
        print('''
          Type Any words......
          to stop write QUIT
          ''')
        
        user_input = input()
        if user_input=='QUIT':
            flag = False
        else:
          file.write(user_input + '\n')

file = open('test_2.txt', 'r')
print('File Contents : ', file.read())

file.close()