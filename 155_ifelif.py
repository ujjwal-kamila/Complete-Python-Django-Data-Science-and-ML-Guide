# 155. The if-elif Statement

def nums_info(a, b):
    if (type(a) is not int) or (type(b) is not int):
        return "One of the arguments is not int"

    if a > b:
        return f"{a} is grater than {b}"
    
    return f"{a} is less than {b}"

print(nums_info(True, 10))
print(nums_info(10, 2))
print(nums_info(4, 15))


# simple calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+ - * /): ")

if op == '+':
    print("Result:", a + b)
elif op == '-':
    print("Result:", a - b)
elif op == '*':
    print("Result:", a * b)
elif op == '/':
    if b == 0:
        print("Cannot divide by zero")
    else:
        print("Result:", a / b)
else:
    print("Invalid operator! try again")


# check alphabet upper case or lowercase
ch = input("Enter a single char : ")

if ch.isupper():
    print("Uppercase letter")
elif ch.islower():
    print("Lowercase letter")
elif ch.isdigit():
    print("It's a digit")
else:
    print("Not a letter")
