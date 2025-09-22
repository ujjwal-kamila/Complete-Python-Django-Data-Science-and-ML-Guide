# 224. Practice - Selective Imports from Other Modules
from utils import * 

my_name = 'Ujjwal'

print(dir())            
print(hello('Ujjwal')) 
print(my_name)        


# math module ex
from math import sqrt, pi 

print(sqrt(16))   
print(pi)         


# random module example
from random import randint, choice

print(randint(1, 10))     
print(choice(['a', 'b']))  


# datetime module example
from datetime import date, timedelta 

today = date.today()  
print(today)                
print(today + timedelta(5))  
