# 190. Generators in For-In Expressions: low mem uses, efficiient loop for large data , useful for big file

'''
syntax:
generator_name = (expression for item in iterable if condition)

'''

# define  tuple 
nums = (2, 6, 9, 10)

# Create a generator expression
squares = (num * num for num in nums)

print(squares)      
print(type(squares))     # <class 'generator'>


# generator expression using range
squares = (x * x for x in range(1, 6))
print(type(squares))     # <class 'generator'>

# Iterate over the generator and print each square
for num in squares:
    print(num)


# convert generator to a tuple using built in tuple 
nums = [2, 5, 9, 10,18]
gen = (num * num for num in nums)
print(type(gen))

# Convert
squares_tuple = tuple(gen)
print(squares_tuple)
print(type(squares_tuple))


# advantage of generator is : SIZE
from sys import getsizeof
sq_gen = (num * num for num in range(100))
print(getsizeof(sq_gen))
print(type(sq_gen))

sq_list = [num * num for num in range(100)]
print(getsizeof(sq_list))
print(type(sq_list))
print(sq_list)