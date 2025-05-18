# 106. Practice - Exploring Docstrings
# check sample docstrings suing ctrl+ click
import math
from datetime import date

# sample example
def max_of_two(a, b):
    """
    Return the maximum of two numbers.

    Args:
        a (int or float): First number.
        b (int or float): Second number.

    Returns:
        int or float: The larger number.
    """
    return a if a > b else b
# test
print("Max of 10 and 20 is:", max_of_two(10, 20)) 


def square(x):
    """
    Return the square of a number.

    Args:
        x (int or float): Number to be squared.

    Returns:
        int or float: Square of x.
    """
    return x * x

# test
print("Square of 5 is:", square(5))     


def greet(name):
    """
    Return a greeting message.

    Args:
        name (str): The name of the person.

    Returns:
        str: Greeting message.
    """
    return f"Hello, {name}!"

# test
print(greet("Python Learner"))


'''
107. Practice - Adding Docstrings to Functions

'''

#  Example— Area of a Circle without docstr:

def area_of_circle(radius):
    return 3.14159 * radius * radius


#  using docstring:

def area_of_circle(radius):
    """
    Calculate the area of a circle given its radius.

    Args:
        radius (float): Radius of the circle.

    Returns:
        float: Area of the circle.
    """
    return 3.14159 * radius * radius

# previous send_email code 
def send_email(to,sub,*args,**kwargs):
    """
    Sends an email to different recipients.

    Args:
        to (str): Primary recipient address
        sub (str): Email subject
        *args (str): Additional recipients
        **kwargs (str): Additional details (like sender, timestamp etc.)

    Returns:
        tuple: A tuple of additional recipients (args)
    """
    
    print(f"Send email to : {to}")
    print(f"Email subject is : {sub}")
    #or can do loop 
    if args:
        print("\nAdditonal argmunets : ",end = ' ')
        for i in args:
            print(i,end ='  ')

    # for kwargs
    if kwargs:
        print("\nKeyword args :")
        for key in list(kwargs):
            print(f"{key} : {kwargs[key]}ṣ")
    
    return args

# test
# send_email (True,100)  ## checking warnings but easyly runs without error 