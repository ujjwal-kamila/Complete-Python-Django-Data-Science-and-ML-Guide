# 137. Practice - Raising Custom Errors

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

res = register_user('ujjwalkamil@.com',21)
print(res)