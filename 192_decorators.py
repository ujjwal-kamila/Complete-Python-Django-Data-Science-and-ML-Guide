# 192. Introduction to Decorator Functions
'''
SYNTAX: use the decorator using @my_decorator 
def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

'''

def decorator_fun(original_fn):
    def wrapper_func(*args, **kwargs):
        print(args)
        print(kwargs)
        # some actions before execution of orignal_fn function
        print("Executed before execution ")

        res = original_fn (*args,**kwargs)
        # some actions after execution of orignal_fn function
        print("Executed after execution ")
        
        return res
    return wrapper_func

# use decorator using @
@decorator_fun
def say_hello(*args,**kwargs):
    print("Hello !")

# Call the function
say_hello(21,name= 'Ujjwal')
