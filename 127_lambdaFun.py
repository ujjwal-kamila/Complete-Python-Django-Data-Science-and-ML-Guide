# 127. Lambda Functions

'''
 Syntax of Lambda Function:

lambda arguments: expression
'''

# regular fun
def mult(a,b):
    return a * b

# lambda fun 
multiply = lambda a,b : a*b
print(multiply(4,5))

# print((lambda a, b: a * b)(4, 5)) 


# filtering data using lambda fun
nums = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)



# greeting function using lambda
def greeting(greet):
    return lambda name: f"{greet}, {name}!"

morning_greeting = greeting("Good Morning")
print(morning_greeting('Ujjwal'))
evening_greeting = greeting("Good Evening")
print(evening_greeting('Ujjwal'))