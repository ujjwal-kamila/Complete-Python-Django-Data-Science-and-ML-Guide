# 17. Code Indentations in python 
# indentation uses 4 whilte spaces for indent to correct the block

def display_name(name):
    print("My name is :",name)
    
name = "Ujjwal"
display_name(name)
upper_name = print(name.upper())
lower_name = print(name.lower())

# gives Indentation Error
# if 5 > 10 :
# print("False")

# correct way to give 4 white space before print fun 
if 5 > 10 :
    print("True")
else :
    print("False")
    
    
    
# another example
def add(a,b):
    return a+b

print(add(3,5))