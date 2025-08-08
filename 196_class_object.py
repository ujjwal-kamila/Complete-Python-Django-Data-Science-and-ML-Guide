# 196. Classes and Objects

'''
Class = Blueprint of an object  
Object = An object is an instance of a class.
'''

# Define a class named Car
class Car:
    def move(self):
        print("Car is moving ")
    
    def stop(self):
        print("Car stopped")

# Create a new object
my_car = Car()

# Check the type of the object
print(type(my_car))  

# Check if my_car is an instance of Car
print(isinstance(my_car, Car))  # True

# Check if my_car is an instance of object 
print(isinstance(my_car, object)) 

# Print all available attributes and methods
print(dir(my_car))

# Print instance variables
print(my_car.__dict__) 

# Call the methods
my_car.move()   
my_car.stop()  
