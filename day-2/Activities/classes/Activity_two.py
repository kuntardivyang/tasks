# Classes 
# Implement a class to represent a Rectangle with methods to calculate area and perimeter.

class Rectangle:
    
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
        
    def calculate_area(self):
        print(f'Area of rectangle {self.breadth*self.length}')
        
    def calculate_perimeter(self):
        perimeter = 2*(self.breadth+self.length)
        print(f'Perimeter of rectangle {perimeter} ')


reactangle_object = Rectangle(5,5)
reactangle_object.calculate_area()
reactangle_object.calculate_perimeter()
print()
