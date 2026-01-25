# 225. Practice - Importing between Different Modules

# main.py

# Import functions
from other import sum_fn, multiply_fn
# alias
import utils as my_utils

# import the entire 'my_module'
import my_module

print(sum_fn(10, 2))

print(my_utils.hello('Ujjwal'))

print(my_module.my_name)


greeting = my_utils.hello("Coders")
print(greeting)