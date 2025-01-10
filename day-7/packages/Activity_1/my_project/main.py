from calculations import arithmetic, geometry

number1 = float(input('Type First Number : '))
number2 = float(input('Type Second Number : '))

print(f'The Addition of Entered Numbers are {arithmetic.add(number1, number2)}')
print(f'The subtraction of Entered Numbers are {arithmetic.subtract(number1, number2)}')
print(f'The Multiplication of Entered Numbers are {arithmetic.multipy(number1, number2)}')
print(f'The Division of Entered Numbers are {arithmetic.division(number1, number2)}')

radius = float(input('Enter radius of a circle : '))
if radius < 0 :
    print('Radius must be positive. ')
else :
    print('The Area Of Circle is ', round(geometry.area_of_circle(radius), 2))
    print('The perimeter Of Circle is ', round(geometry.perimeter_of_circle(radius), 2))
    
length = float(input('Enter length of a rectangle : '))
breadth = float(input('Enter breadth of a rectangle : '))

if (length < 0 or breadth < 0):
    print('length or breadth cant be less then zero. ')
else :
    print('The Area of rectangle is : ', geometry.area_of_rectangle(length, breadth))
    print('The Perimeter of rectangle is : ', geometry.perimeter_of_rectangle(length, breadth))