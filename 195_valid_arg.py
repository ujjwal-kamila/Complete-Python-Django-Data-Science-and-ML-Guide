# 195. Example - Validating Arguments with Decorator Functions

# use decorator fun for checking types in a fun 
def valid_args(fn):
    def wrapper(*args,**kwargs):
        for arg in args:
            if not isinstance(arg,int):
                raise ValueError("Argumnets must be integers!",f"{arg} is of type {type(arg)} ")
        return fn(*args, **kwargs)

    return wrapper

@valid_args
def sum(a,b):
    return a+b

# handle the type error 
try:
    res = sum(5,8)
    print("Result is : ",res)

    res= sum('5',6)
    print("Result is : ",res)
except ValueError as e :
    print(e)

