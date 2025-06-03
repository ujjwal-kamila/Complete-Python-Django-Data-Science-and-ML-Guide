# 136. Example - Handling Undefined Variable Errors

# Trying to print a variable that is not defined
try:
    print(value)  

except NameError:
    print("Error: The variable is not defined!")

except Exception as e:
    print("Some other error occurred:", e)

else:
    print("Variable printed successfully!")

finally:
    print("Program execution completed.")


# in finally block always close the file 
try:
    file = open("file.txt", "r")  
except FileNotFoundError as e:
    print(e) 
else:
    print("File is ready for reading")
    print("File contains... \n")
    print(file.read())
finally:
# Checks if the variable named file exists in the global scope.
    if 'file' in globals() and file and not file.closed:
        file.close()
        print("\n...........")
        print("File was closed.")
        print(file.closed)
