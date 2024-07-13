# 41. Practice - Alternative String Formatting Methods


name = 'Ujjwal Kamila'
hometown = 'Jhargram'
age = 19

info = f"My name is {name} \nI am from {hometown} and my age is {age}"
print(info)

# using format operator 
info1  = "My name is {} \n I am from {} and my age is {} ".format(name, hometown, age)
print(info1)

print('\n')

info2 = "My name is %s \n I am from %s and my age is %s " %(name, hometown, age)
print(info2)