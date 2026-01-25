# 226. Practice - Modules in Subfolders

# main.py

# import specific function from the 'src' folder
from src.other import sum_fn

# import 'utils' from 'src' 
import src.utils as my_utils

# import 'my_module' from 'src' 
import src.my_module as my_module


# Use the math function
print(sum_fn(10, 2))

# Use the hello function 
print(my_utils.hello('Bogdan'))

# Access the variable
print(my_module.my_name)
