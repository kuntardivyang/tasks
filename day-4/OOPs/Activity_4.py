# Create a Shape parent class and Circle and Square child classes, each with its own method to calculate the area.
from math import pi

class Shape:
    def __init__(self,length):
        self.length = length
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius)
        
    def calculate_area(self):
        area = pi*self.length**2
        print('Area Of Circle : ', round(area,2))

class Square(Shape):
    def __init__(self, length):
        super().__init__(length)

    def calculate_area(self):
        area = self.length**2
        print('Area Of Square : ', round(area,2))

circle1 = Circle(5)
square1 = Square(10)

circle1.calculate_area()
square1.calculate_area()