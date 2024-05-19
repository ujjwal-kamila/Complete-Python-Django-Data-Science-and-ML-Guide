#13 Return Statement functions 

#  multiply function 
def multiply_numbers(a,b):
    result = a*b
    return result

result_mul = multiply_numbers(5,6)
print("Multiplication result is : ",result_mul)
print(multiply_numbers(5,5))

# add function

def add_num(x,y):
    res = x+y
    return res
add_res = add_num(5,10)
print("Sum is :",add_res)