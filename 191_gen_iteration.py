# 191. Practice - Generators and Iteration over the Generator
'''
Generator uses less memory than list.
List stores all values, generator does not.
'''

# import getsizeof for get the size 
from sys import getsizeof

# get the even numbers generator variable
even_generator = (num for num in range(1000) if num % 2 == 0)

# check the size 
print("Size of generator object:", getsizeof(even_generator))  # 200 small memory

# check the type
print("Type of even_generator:", type(even_generator)) 

# Creating a list comprehension 
even_gen_list = [num for num in range(1000) if num % 2 == 0]

# Measuring memory size 
print("Size of list object:", getsizeof(even_gen_list))   # 4216 more memory

# checking the type
print("Type of even_gen_list:", type(even_gen_list))



# Create a generator 
squares_gen = (num * num for num in range(100_000_000))

# Iterate through the generator
for num in squares_gen:
    print(num)  
    if num == 100:
        break 
    
# start second iteration
print("\nStart 2nd loop")
'''
After the first loop, the generator is exhausted (used up), so the second loop does nothing unless you create the generator again
'''
# The second loop continues from where the generator was left off
for num in squares_gen:
    print(num)  
    if num == 225:
        break 


print()
print()
# In case of list 
# Create a list of squares
squares_list = [num * num for num in range(100)]

# First iteration 
for num in squares_list:
    print(num)
    if num == 25:
        break

# Start second iteration from the beginning
print("\nStart 2nd Loop\n")

for num in squares_list:
    print(num)
    if num == 100:
        break
