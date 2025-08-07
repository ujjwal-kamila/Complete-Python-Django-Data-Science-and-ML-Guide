# 194. Example - Logging using Decorator Functions

def log_fun_call(fn):
    def wrapper(*args,**kwargs):
        print(f"Calling function {fn.__name__}")
        print(f"funcion args : {args}, {kwargs}")
        
        res = fn(*args, **kwargs)
        print("Result of the function is : ",res)
        return res
    
    return wrapper


@log_fun_call
def mult_number(a,b):
    return a*b

print(mult_number(10,5))
print('')

# let's use decorator in another fun
@log_fun_call
def sum_nums(a,b):
    return a+b

print(sum_nums(10,15))
print('')
print(sum_nums(a=5,b=10))
