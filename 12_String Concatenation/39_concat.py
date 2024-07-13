# 39. Practice - Concatenating Strings using the + Operator

# we can conacat str using f-strings don't need to use any operator 

name = 'Ujjwal'
hometown = 'Jhargram'
age = 19
# using concat operator 
info ="My name is "+ name +"\n" + 'I am from ' +hometown +' and my age is : '+str(age)
print(info)
print("\nUsing f-string \n")
# using f strings 
info1 = f"My name is {name} \nI am from {hometown} and my age is {age}"
print(info1)

# f str line is short then operator one 