# 219. Inheritance in Object-Oriented Programming (OOP)

# simple example 
# Parent class
class Vehicle:
    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"{self.name} is starting...")

    def stop(self):
        print(f"{self.name} is stopping...")

# Child class (inherits Vehicle)
class Car(Vehicle):
    def __init__(self, name, brand):
        super().__init__(name)  # call parent constructor
        self.brand = brand

    def honk(self):
        print(f"{self.brand} {self.name} goes 'Beep Beep!'")

# Example
v1 = Vehicle("Bike")
v1.start()
v1.stop()

print()
'''Car gets start() and stop() from Vehicle and adds honk()'''
c1 = Car("Model S", "Tesla")
 # from Vehicle
c1.start()  
c1.honk()    # from Car
c1.stop()    # from Vehicle





# Type of Inheritance Single ,Multiple,Multilevel ,Hiearchical 

''' Single Inheritance : Parent → Child'''
print("\nSingle Inheritance Eg :")
class Parent:
    def __init__(self, name):
        self.name = name

    def display(self):
        return f"Parent name : {self.name}"

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def show(self):
        return f"Child name : {self.name}, Age : {self.age}"

c1 = Child("Raj", 5)
print(c1.display())  # Parent's method
print(c1.show())     # Child's method




''' Multiple Inheritance : Parent1, Parent2 → Child'''
print("\nMultiple Inheritance Eg :")

# Example: Processor,Battery → Phone

class Processor:
    def __init__(self, speed):
        self.speed = speed

    def processor_info(self):
        return f"Processor Speed: {self.speed} GHz"

class Battery:
    def __init__(self, capacity):
        self.capacity = capacity

    def battery_info(self):
        return f"Battery Capacity: {self.capacity} mAh"

class Phone(Processor, Battery):
    def __init__(self, speed, capacity, brand):
        Processor.__init__(self, speed)
        Battery.__init__(self, capacity)
        self.brand = brand

    def phone_info(self):
        return f"{self.brand} Phone with {self.speed} GHz processor and {self.capacity} mAh battery"

phone = Phone(3.5, 5000, "Samsung")
print(phone.processor_info())
print(phone.battery_info())
print(phone.phone_info())




''' Multilevel Inheritance : Grandparent -> Parent ->  Child '''
print("\nMultilevel Inheritance Eg :")

# Example: Animal → Mammal → Dog

class Animal:
    def __init__(self):
        print("This is an Animal ")

    def breathe(self):
        return "Breathing..."

class Mammal(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("This is a Mammal")

    def walk(self):
        return "Walking on land"

class Dog(Mammal):
    def __init__(self):
        Mammal.__init__(self)
        print("This is a Dog")

    def bark(self):
        return "Barking..."

dog = Dog()
print(dog.breathe())
print(dog.walk())
print(dog.bark())




''' Hierarchical Inheritance : Parent → Child1, Child2 '''
print("\nHierarchical Inheritance Eg :")
# Example : Vehicle -> Car, Bike

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def vehicle_info(self):
        return f"This is a {self.brand} vehicle."

class Car(Vehicle):
    def __init__(self, brand, seats):
        Vehicle.__init__(self, brand)
        self.seats = seats

    def car_info(self):
        return f"{self.brand} Car with {self.seats} seats."

class Bike(Vehicle):
    def __init__(self, brand, type):
        Vehicle.__init__(self, brand)
        self.type = type  # Example: Sports or Cruiser

    def bike_info(self):
        return f"{self.brand} Bike of {self.type} type."

c = Car("Toyota", 5)
b = Bike("Yamaha", "Sports")

print(c.vehicle_info(), c.car_info())
print(b.vehicle_info(), b.bike_info())






''' Hybrid Inheritance : Parent1 → Child1, Parent2 → Child2 → Grandchild '''
print("\nHybrid Inheritance Eg :")

# Example: Person -> Student, Teacher -> TeachingAssistant
class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"Name: {self.name}"

class Student(Person):
    def __init__(self, name, grade):
        Person.__init__(self, name)  # Corrected
        self.grade = grade

    def study(self):
        return f"{self.name} is studying in grade {self.grade}th"

class Teacher(Person):
    def __init__(self, name, subject):
        Person.__init__(self, name)  # Corrected
        self.subject = subject

    def teach(self):
        return f"{self.name} is teaching {self.subject}"

class TeachingAssistant(Student, Teacher):
    def __init__(self, name, grade, subject):
        Student.__init__(self, name, grade)
        Teacher.__init__(self, name, subject)



ta = TeachingAssistant("John", 12, "Math")
print(ta.info())
print(ta.study())
print(ta.teach())
