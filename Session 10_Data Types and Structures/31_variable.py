# 31. Variables and Objects

# We can print location using id(var)

# Examples

my_name = 'Ujjwal'
print("Address is :",id(my_name))
# Address is : 1922584056608

my_full_name = "Ujjwal Kamila"
print("Address is :",id(my_full_name))
# Address is : 1922584243568



# Variables can also refer to one object 
'''
when they are assigned to each other or
when they are created in a way that makes
them reference the same memory location
'''
# Examples
# Create an integer
a = 10
# Assign a to b
b = a
# Print addresses
print("Address of a:", id(a))
print("Address of b:", id(b))

# Check if they are the same object
print("a and b refer to the same object:", a is b)

# Another example
# Create a list
list1 = [1,2,3,4,5,6,7,8]

# Assign list1 to list2
list2 = list1

# Print Address
print("Address of List1 :",id(list1))
print("Address of List2 :",id(list2))

# Check if they are the same object
print("list1 and list2 refer to the same object:", list1 is list2)