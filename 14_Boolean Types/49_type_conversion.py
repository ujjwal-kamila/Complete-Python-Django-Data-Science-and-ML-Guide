# # 49. Type Conversion

# # Type conversion is nessesary for operations & handle correct data types 
# # print(10 + '5')  # type error 
# print( 10 + int('5'))

# # more examples 
# int_num = 5
# float_num = 3.14
# print(f"sum of {int_num} and {float_num} is :",int_num+float_num)

# # how the addition performed "magic method"
# print(int_num.__add__(float_num))    # NoImplemented 
# print(float_num.__radd__(int_num))   # 8.14


# # True indicate one value
# bool_val = True
# int_val = 10
# print(f"Sum of {bool_val} and {int_val} is :",bool_val+int_val)
# print('\n\n')


# # 50.Magic Methods 

# # all magic operators in python
# '''
#     __add__()
#     __eq__()
#     __and__()
#     __str__()
#     __neq__()
#     __or__()
    
# '''

# # 51. Practice - Utilizing Magic Attributes and Methods
# my_str = 'ABC'
# # Print all available methods and attributes of an object
# # Example with a string object:
# # print(dir(my_str))

# # Print all methods of the str class using "dir(str)"
# # print(dir(str))

# # Print the documentation of the str class
# print(str.__doc__)
# # Same as bool
# print(bool.__doc__)

# # Comparison between two numbers 
# num = 100
# other_num = 100
# print(num.__eq__(other_num))
# # Same using comparison operator 
# print(num == other_num)

# # To get help or descrption of the methods "help()"
# print(help(num.__add__))


# Let's make an class that constaints all magic methods
class Magic:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Magic(self.value + other.value)

    def __eq__(self, other):
        return self.value == other.value

    def __and__(self, other):
        return Magic(self.value & other.value)

    def __or__(self, other):
        return Magic(self.value | other.value)

    def __ne__(self, other):
        return self.value != other.value

    def __str__(self):
        return f"Magic({self.value})"


# Creating instances
obj1 = Magic(5)
obj2 = Magic(3)

# Using __add__()
add_result = obj1 + obj2
print("Addition Result:", add_result)  

    # Using __eq__()
eq_result = obj1 == obj2
print("Equality Result:", eq_result)  

# Using __and__()
and_result = obj1 & obj2
print("Bitwise AND Result:", and_result)  
# Using __or__()
or_result = obj1 | obj2
print("Bitwise OR Result:", or_result)  
# Using __ne__()
ne_result = obj1 != obj2
print("Inequality Result:", ne_result)  

# Using __str__()
str_result = str(obj1)
print("String Representation:", str_result) 