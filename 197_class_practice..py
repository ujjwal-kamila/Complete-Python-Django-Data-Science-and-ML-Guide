# 197. Practice - Understanding Classes and Class Instances

# Create a class car with attribute like brand and model.Then create instance of this class

# Define the Car class
class Car:
    def __init__(self, brand, model, color, price, top_speed):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.top_speed = top_speed 

    # Start the car
    def start(self):
        print(f"{self.brand} {self.model} is starting with a key... ")

    # Stop the car
    def stop(self):
        print(f"{self.brand} {self.model} has stopped.⛔")

    # Print car info
    def print_info(self):
        print(f"Car Details: \n {self.brand} {self.model}, Color: {self.color}, Price: ${self.price}, Top Speed: {self.top_speed} km/h\n")

# Create an object (instance) of the Car class
my_car = Car("Toyota", "Corolla", "Red", 20000, 300)

# Call methods
my_car.print_info()
my_car.start()
my_car.stop()

# new Object 
s = Car("BMW", "M4", "Black", 70000, 280)
s.print_info()
s.start()
s.stop()