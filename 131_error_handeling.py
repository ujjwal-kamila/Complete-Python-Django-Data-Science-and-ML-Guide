# 131. Error Handling
'''
try:
    # risky code
except SomeError:
    # runs if error occurs
else:
    # runs if no error
finally:
    # runs no matter what

'''
# a = 10/0   # zero divisional error
try:
    print(10/0)
except ZeroDivisionError:
    print("Error - Division by zero")
print("Hello")


try:
    print('5'/0)
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("There is no Erro!")
finally:
    print("Continue ")

# catching any error 
try:
    print(3.14+'ujjwal')
except Exception as e:
    print(e)
    
    
# Error generation with raise
def divide_nums(a,b):
    if b == 0:
        raise TypeError("Second argument cannot be 0...")
    return a/b

try:
    res = divide_nums(12,0)
    print(res)
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)


print("continue")

