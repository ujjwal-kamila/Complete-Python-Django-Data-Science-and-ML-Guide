# 138. Practice - Handling Raised Errors using Try and Except

def contains_any_symbol(email):
    return '@' in email

def register_user(email,age):
    if not isinstance(email,str):
        raise TypeError("Email must be a string!")
    
    if not isinstance(age,int):
        raise TypeError("Age must be an integer ")
    
    if not contains_any_symbol(email):
        raise ValueError("Invalid Email <must contain '@' sign>")
    print("User Registered Sucessfully!..")
    return { 'email': email, 'age': age}

# using try catch block
try:
    res = register_user('ujjwal@gmail.com',21)
    print(res)
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)

# Raise custom exception

class UnderAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise UnderAgeError("User is under age!")
    print("Access granted.")

try:
    check_age(17)
except UnderAgeError as e:
    print("Access denied:", e)
