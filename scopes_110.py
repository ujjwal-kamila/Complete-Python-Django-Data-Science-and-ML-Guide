# 110. Scopes : Boundary for specific variable

# Global variable: defined outside any function
x = 10  

def show():
    # Local variable: defined inside the function
    y = 5
    print("Inside function -> x:", x)  # accesses global x
    print("Inside function -> y:", y)  # accesses local y

show()

# Outside the function, only x is accessible
print("Outside function -> x:", x)
# print(y)  #  error 


# example : scope chain
'''
Two type of scopes : Global and local(fucntion)'''
x = "global"  # Global Scope

def outer():
    x = "enclosing"  # Enclosing Scope 

    def inner():
        x = "local"  # Local Scope
        print("Inside inner:", x)

    inner()

outer()
print("In global scope:", x)
