# 114. Operators
# Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operators:")
print()
print("Addition:", a + b)         
print("Subtraction:", a - b)      
print("Multiplication:", a * b)   
print("Division:", a / b)         
print("Floor Division:", a // b)  
print("Modulus:", a % b)          
print("Exponent:", a ** b)        
print()

# Assignment Operators
x = 5
print("Assignment Operators:")
print()
x += 2     
print("x += 2:", x)
x -= 1     
print("x -= 1:", x)
x *= 3     
print("x *= 3:", x) 
x /= 2     
print("x /= 2:", x)  
x %= 4     
print("x %= 4:", x)  
print()

# Comparison Operators
a = 5
b = 10
print("Comparison Operators:")
print()
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)  
print("a < b:", a < b) 
print("a >= b:", a >= b)
print("a <= b:", a <= b)
print()

# Logical Operators
x = True
y = False
print("Logical Operators:")
print()
print("x and y:", x and y)
print("x or y:", x or y) 
print("not x:", not x)    
print()

# Bitwise Operators
a = 5       # 0101 
b = 3       # 0011
print("Bitwise Operators:")
print()
print("a & b:", a & b)   
print("a | b:", a | b)   
print("a ^ b:", a ^ b)   
print("~a:", ~a)         
print("a << 1:", a << 1) #
print("a >> 1:", a >> 1) 
print()

# Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("Identity Operators:")
print()
print("a is b:", a is b)
print("a is c:", a is c)    
print("a is not c:", a is not c)
print()

# Membership Operators
nums = [1, 2, 3, 4]
print("Membership Operators:")
print()
print("2 in nums:", 2 in nums)     
print("5 not in nums:", 5 not in nums)