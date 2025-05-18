# 104. Docstrings : used to document funtions classes and modules
"""

format is that inverted(single or double) comma 3 times 

& ✅ Clearly documented parameters, returns, and exceptions 
"""
# example
def fact(n):
    """
    Calculate the factorial of a non-negative integer n using recursion.
    
    Parameters:
    n (int): A non-negative integer
    
    Returns:
    int: Factorial of n


    Raises:
    ValueError: If n is negative

    Example:
    >>> factorial(5)
    120
    """
    if n < 0:
        raise ValueError("Negative number!")

    if n==0 or n==1 :
        return 1
    return n * fact(n-1)


# test
print(f"Fact of 5 is : ",fact(5))
print(f"Fact of 5 is : ",fact(3))

# ex: odd even fun 

def odd_even(num):
    """
    prints whether a number is even or odd

    Args:
        num (int): number to be checked via fun 
    """
    if (num %2) == 0 :
        print(f"The number {num} is Even ")
    else:
        print(f"The number {num} is Odd")

'''test'''

res = odd_even(20)




# 105. Practice - Writing and Using Docstrings

# sample function with docstring
def function_name(parameters):
    """
    One-liner summary of the function.

    Optional extended description of the function's behavior.

    Parameters:
        param1 (type): Description of param1
        param2 (type): Description of param2

    Returns:
        type: Description of the return value

    Raises:
        ErrorType: Condition when the error is raised

    Example:
        >>> function_name(2, 3)
        5
    """
    # function body
    
    
# example function with docstring
def add(a, b):
    """
    Add two numbers.

    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.

    Example:
        >>> add(3, 5)
        8
    """
    return a + b




