# Write a program to:
# Use deque to implement a queue with the ability to add and remove elements from both ends.
# Rotate the deque and display the results.
from collections import deque
import time
elements = deque()
while True:
    print('''
            Type 1 to Add Element at left
            Type 2 to Add Element at right
            Type 3 to remove an Element from left
            Type 4 to remove an Element from right
            Type 5 to rotate the deque
            Type 6 for Displaying the deque
            Type 7 for exit
          ''')
    user_input = int(input())
    if user_input == 1:
        add_input = input('Enter An Element to add : ')
        elements.appendleft(add_input)
    elif user_input == 2:
        add_input = input('Enter An Element to add : ')
        elements.append(add_input)
    elif user_input == 3:
        print('Element removed from left ', elements.popleft())
    elif user_input == 4:
        print('Element removed from right ', elements.pop())
    elif user_input == 5:
        elements.rotate(len(elements) - 1)
        print('Rotated ', elements)
    elif user_input == 6:
        print(elements)
        time.sleep(2)
    elif user_input == 7:
        break