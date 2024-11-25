# 82. Understanding Immutable Objects in Python

num1 = 10
num2 = num1 

print(id(num1))
print(id(num2))

num2 = num2 + 10
print(num2)     #20
print(num1)     #10

print(id(num1))
print(id(num2))
