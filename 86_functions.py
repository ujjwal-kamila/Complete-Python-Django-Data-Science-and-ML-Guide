# 86. Functions : Block of code can executed many times
def sum(a,b):
    return a+b
a = 10
b = 5
print(f"sum of {a} + {b} is ",sum(a,b))

# swap two numbers without using third variable
def swap(a,b):
    a = a+b
    b = a-b
    a = a-b
    return a , b

a = 5
b = 4
print(f"Before swap a = {a},b = {b} ")
a,b = swap(a,b)
print(f"After swap a = {a},b = {b} ")

# 87. Calling Functions: Arguments vs Parameters

# sample examples
def my_fun(a,b):
    a = a+1
    c = a+b
    return c

result = my_fun(5,8)
print(result)

# 88. Shortest Function in Python
# examples
def new_fun():
    pass
print(new_fun())        # return None

# more examples
def sum(a,b): return a*b
def show(a,b) : return a , b