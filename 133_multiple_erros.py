# 133. Practice - Using Multiple Error Classes in one Except Block and Parent Exception

try:
    filename = input("Enter filename: ")
    f = open(filename, "r")
    
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    
    result = num1 / num2
    print("Result:", result)

# Handling multiple errors
except (ValueError, FileNotFoundError) as e:
    print("Handled error:", e)

# ZeroDivisionError
except ZeroDivisionError:
    print("You cannot divide by zero.")

# Any other exception
except Exception as e:
    print("Unexpected error:", e)

# Runs if no exception occurs
else:
    print("Everything worked smoothly!")

# Runs always
finally:
    print("Program finished.")
