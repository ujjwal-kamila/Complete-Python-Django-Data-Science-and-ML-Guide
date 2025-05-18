# 115. Unary and Binary Operators
'''
Unary Operator: Works with only one operand ,Ex: -x, ~x
Binary Operator: Works with two operands 
'''

# Unary Operators
print("Unary Operators:")
x = 5
print("Original x:", x)
print("Unary minus -x:", -x)        # -5 (negation)
print("Bitwise NOT ~x:", ~x)        # -6 (bitwise NOT)
print("Logical NOT not True:", not True)  # False
print()

# Binary Operators
print("Binary Operators:")
a = 10
b = 3
print("a + b:", a + b)    
print("a - b:", a - b)      
print("a * b:", a * b)     
print("a > b:", a > b)  
print("a and b:", a and b)  
print("a == b ??", a==b)  


# in and not in operators
car = {
    'brand':'Bugatti',
    'price ':25_0000000
}
print('brand' in car) 
print('year' in car) 
print('year' not in car) 

# precidence of operators
result = ((2 + 3) * (4 + (5 * 2))) - 10
print("Result:", result)
