# 227. Built-in Modules

# math modules
import math as m

print(type(m))
# all functions inside the module
print(dir(m))
# can do also 
# from math import pi
print(m.pi)

# os module
import os
#folder path
print(os.getcwd())  

# radom modules
import random
print(random.randint(1, 10))

# csv: Read and write files.
import csv


import time
# sleep for 2 sec
time.sleep(2)


import time

print("Starting the timer...")
# Pause for 5 seconds
time.sleep(5)

print("Finish! 5 Sec completed..")



# simple dice roll
import random as rd 
import time as tm

print("Rolling the dice...")
tm.sleep(2)  # Wait 2 seconds

# Pick a random number between 1 and 6
result = rd.randint(1, 6)
print(f"You rolled a: {result}")