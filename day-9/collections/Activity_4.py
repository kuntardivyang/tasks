# Use namedtuple to:
# Create a Point class and calculate the distance between two points.
from collections import namedtuple
from math import sqrt
Point = namedtuple('Point', ['x', 'y'])
try:
    def distance(point1, point2):
        return sqrt((point2.x - point1.x)**2 + (point2.y - point1.y)**2)

    point_1 = Point(*map(int, input('Enter Point 1\'s x and y in separated spaces e.g. \'2 3\' ) : ').strip().split()))
    point_2 = Point(*map(int, input('Enter Point 2\'s x and y in separated spaces e.g. \'2 3\' ) : ').strip().split()))

    distance = distance(point_1, point_2)
    print(f"The distance between point 1 and point 2 is {distance:.2f}")

    Student = namedtuple('Student', ['name', 'age', 'grade'])
    students = []
    for i in range(2): 
        name = input('Enter Student\'s name: ') 
        age = int(input('Enter Age: ')) 
        grade = input('Enter Grade: ') 
        student = Student(name=name, age=age, grade=grade) 
        students.append(student) 
    for student in students: 
        print(f"Student Name: {student.name}, Age: {student.age}, Grade: {student.grade}")
except ValueError as e:
    print(e)
    print('Invalid Input')
except Exception as e:
    print(e)