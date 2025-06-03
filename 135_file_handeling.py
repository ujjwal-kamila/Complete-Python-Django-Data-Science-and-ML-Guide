# 135. Example - Handling File Not Found Errors

# simple example
try:
    filename = input("Enter the filename to open: ")
    file = open(filename, "r")  
    content = file.read()
    print("File content:")
    print(content)

except FileNotFoundError:
    print("Error: The file you are trying to open does not exist!")

except Exception as e:
    print("Some other error occurred:", e)

else:
    print("File read successfully!")

finally:
    try:
        file.close() 
        print("File closed.")
    except NameError:
        pass
    print("File operation complete.")


