import my_module  
# info
print(my_module)  

# type 
print(type(my_module))  

# list of names
print(dir(my_module))  

# calls greet 
print(my_module.greet(my_module.my_name))  

# print name
print(my_module.my_name)     

# call greet directly
my_module.greet("Ujjwal")    


# # import the module as shorthand
import my_module as m  

# print module details
print(type(m))
print(dir(m))

# call greet with stored name
print(m.greet(m.my_name))
