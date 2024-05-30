# 27.Variables 

# Think of variables like containers where we store things as like we store out favourite toys in a toy box

name = 'Ujjwal'
print("My name is :",name)

# "snake_case" notation for : [functions,variables,modules,methods]  like example
# Functions and variables use snake_case notation
def calculate_area(radius):
    return PI * radius ** 2

def calculate_circumference(radius):
    return 2 * PI * radius


# "PascalCase" notation for : [User Defined Classes]
# User defined classes use PascalCase notation
class UserProfile:
    def __init__(self, name, age):
        # Variables use snake_case notation
        self.name = name
        self.age = age
    

# "my_package" notation for : [packages]
# Importing from my_package (package notation)
# from my_package.constants import DB_PASSWORD, PI

# "DB_PASSWORD" notation for : [constant variables ]
# Constants use UPPER_CASE notation
PI = 3.14159
MAX_CONNECTIONS = 100
DB_PASSWORD = "my_secret_password"


# checking types 
my_number = 10 
print(type(my_number))

string = 'abc'
print(type(string))