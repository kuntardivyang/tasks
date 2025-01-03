# Create a file reader that catches FileNotFoundError and prompts the user for a new file path.
# 


try:
  file = open('te.txt', 'r')
except FileNotFoundError as e:
  print(e)
  print('File Not Found')
  file_path = input('Enter New Path : ( e.g. test.txt )  ').strip()

file = open(file_path, 'r')
print(file.read())

file.close()