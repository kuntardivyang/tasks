# Import the math module and calculate the area of a circle given its radius.
# Use the random module to simulate rolling a dice 10 times.
import math
import random

radius = float(input('Enter Radius Of Circle to calculate area of it. : '))
area = math.pi * radius ** 2
print(f'Area of circle : {round(area, 2)} ')
        
for i in range(10):
    number = random.randrange(1, 7)
    print(f'Dice Roll turn {i + 1} : {number}')