# 134. Practice - Using Else and Finally Blocks
'''
else : executed when no errors 
finally: always prints'''

'''
try:
    # risky code
except SomeError:
    # runs if error occurs
else:
    # runs if no error occurs
finally:
    # runs no matter what
'''


# simple example
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter integers only.")
else:
    print("Division Result is:", result)
finally:
    print("Program complete...!")


# character to interger conversion using Ascii values
try:
    char_input = input("Enter a single character : ")
    if len(char_input) != 1:
        raise ValueError("Please enter only one character..")
    if char_input.isdigit():
        raise ValueError("Digits are not allowed. Enter only single character like 'a'.")
    ascii_val = ord(char_input)          # ord returns ascii int
except ValueError as e:
    print("Some error ocurred !",e)
else:
    print(f"The ASCII Value of {char_input} is :",ascii_val)
finally:
    print("Conversion Completed..!")