# Write a Python Program to implement Method Overloading and Method Overriding.
class Animal:
    def __init__(self,name):
        self.name = name

    def get_name(self):
        return self.name
    
class Dog(Animal):
    # Overriding the method of Animal class
    def get_name(self):
        return self.name
    
class Cat(Animal):
    # Overriding the method of Animal class
    def get_name(self):
        return self.name

dog1 = Dog('Tommy')
cat1 = Cat('Meow')

print(dog1.get_name())
print(cat1.get_name())


# Method Overloading Example