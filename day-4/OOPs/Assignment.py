class Student:
    total_stud=0
    def __init__(self,name,grade,marks):
        self.name = name
        self.grade = grade
        self.science = marks[0]
        self.maths = marks[1]
        self.english = marks[2]
        Student.total_stud += 1
        
    @classmethod
    def total_student(cls):
        print('Total Students is : ', Student.total_stud)
    
    def total_and_average(self):
        total_marks = self.science + self.english + self.maths
        print('Total Marks : ', total_marks)
        print('Average of marks : ', round(total_marks/3, 2))
        
class Scholar(Student):
    def __init__(self,name,grade,marks,scholarship):
        super().__init__(name,grade,marks)
        self.scholarship=scholarship

    def display_details(self):
        print('Scholarship Amount : ', self.scholarship)

obj1 = Student('Smit Kuntar', 'A', [78, 79, 60])
obj2 = Scholar('Divyang Kuntar', 'B',[98, 99, 100], 85000)
obj1.total_student()
obj2.total_and_average()
obj2.display_details()
