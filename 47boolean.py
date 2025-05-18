# 47. Boolean Values

# Return True or False
is_even = True
print(is_even)
print(type(is_even))

# some more examples
print(5>4)   # True 
print(-10 > 5)  # False
print('Hello World!' > "Hello")     # True 
print([1,2,3,4,5] == [1,2,3,4,5])   # True 

# Conversion to a boolean value "bool(my_value)"
my_value = []
print(bool(my_value))    # False 
name = 'Ujjwal'
print(bool(name))       # True 





# 48. Practice - Working with Boolean Values
print("\n\nPractice - Working with Boolean Values\n")

# let's check that is an instance or not 
data_is_available = False
print(data_is_available)
print(type(data_is_available))
# Checking instance or not 
print(isinstance(data_is_available , bool))

# Convert values of other type to boolean type
print(bool(''))  # False 
print(bool(0))   # False 
print(bool(0.00000))     # False 
print(bool('hello'))    # True 
print(bool([]))  # False 
print(bool([1,2,3]))    # True     

# So if we convert non boolean value to boolean get True or False
# some expression reults 
print(100 > 10)
print(100 == 100)
print([1,2,4] ==[[2,4,5,6]])
print([9,8,7] == [9,8,7])

is_available = True
print(not is_available)

my_name ='Ujjwal' 
print(is_available and my_name)
# Convert it to boolean
if is_available and my_name:
    print("Is avilable")
