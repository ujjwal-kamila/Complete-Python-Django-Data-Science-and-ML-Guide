# 139. Practice - Specifying Types for Function Parameters

#  Check if input is integer and non-negative
def calculate_square(n):
    if not isinstance(n, int):
        raise TypeError("Only integers are allowed")
    if n < 0:
        raise ValueError("Only non-negative numbers are allowed")
    return n ** 2

try:
    print(calculate_square(4))
    print(calculate_square(-5))
except Exception as e:
    print("Error:", e)


# type hints
def greet(name: str) -> None:
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    print(f"Hello, {name}!")

try:
    greet("Ujjwal")
    greet(123)
except Exception as e:
    print("Error:", e)



# password validator 
def set_password(password: str):
    if not isinstance(password, str):
        raise TypeError("Password must be a string")
    if len(password) < 6:
        raise ValueError("Password must be at least 6 characters long")
    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one number")
    print("Password accepted.")

try:
    set_password("abc12")
except Exception as e:
    print("Error:", e)

