# 32. Practice - Using the built-in id() Function

# Printing id of print function 
print(id(print))

# Crate a var and print id of that
my_name = "Ujjwal"
print()

# Print addresses
print("Address of a:", id(my_name))

num = 1000
print("Address is num is  :",id(num))

# the address will remain same as upper addres
other_num = num 
print("Address of other num ",id(other_num))

