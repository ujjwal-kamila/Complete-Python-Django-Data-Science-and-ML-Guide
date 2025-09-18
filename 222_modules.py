# 222. Modules
'''
Avoid to duplication of the code blocks
import using 'import module_name'
'''

# Standard Module (built-in)
import math
print("Standard Module Example:")
print(math.sqrt(16))  # from math

# User-defined Module
import my_module  # own local Python file
print("User-defined Module Example:")
my_module.greet("Ujjwal")


# Third-party Module
import requests  # Installed via pip
print("Third-party Module Example:")
response = requests.get("https://example.com")  # sample
print(response.status_code)

# Package (collection of modules)
from math import sqrt, pow
print("Package Example:")
print(sqrt(25))  # from math package
print(pow(2, 3))  # from math package
