# 220. Polymorphism in Object-Oriented Programming (OOP)

import math

# Main class
class Shape:
    def calc_area(self):
        # overridden 
        pass

# Derived class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return math.pi * (self.radius ** 2)

# Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_area(self):
        return self.length * self.width

# Create a list of shapes
shapes = [Circle(5), Rectangle(10,2), Circle(3),Rectangle(25,15)]

'''
Same method is used in different classes but it works
'''

for shape in shapes:
    print(f"Area:{shape.calc_area():.2f}")

