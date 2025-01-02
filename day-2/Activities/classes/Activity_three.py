# Classes 

# 3.Create a Student class with attributes for name, age, and grades. Add methods to calculate average grade and display student details.

class Student:
    def __init__(self,name,age,grades):
        self.name = name
        self.age = age
        self.grades = grades
    
    def student_detail(self):
        print(f'Name : {self.name}')
        print(f'Age : {self.age}')
        print(f'grades : {self.grades}')

    def average_grades(self):
        print('Average of grades : ', int(sum(self.grades)/len(self.grades)))


student_object=Student('Divyang', '20', [100, 99, 98, 99, 97, 96])
student_object.student_detail()
student_object.average_grades()
