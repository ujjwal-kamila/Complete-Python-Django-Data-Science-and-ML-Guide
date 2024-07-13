# 37. Practice - String Methods

# Input Str 
my_com = "This is a short comment "
print("Input comment:", my_com)

# Prints the string length  
print("Length of given string is:", len(my_com))

# Replace 'short' with 'long'
new_com = my_com.replace("short", "long")
print("After replacing:", new_com)

# Count occurrences of the substring 'is'
count_is = my_com.count('is')
print("Occurrences of 'is':", count_is)

# Access specific characters by index [Start: End: Step value]
print("Substring from index 8 to 21:", my_com[8:21])

# Reverse the whole string
print("Reversed string:", my_com[::-1])

# Find index of substring 'short'
print("Index of 'short':", my_com.find('short'))

# If substring not present in string then give '-1'
print("Index of 'hii' (not present):", my_com.find('hii'))  # -1

# Split the whole string with given input
print("Splitting by spaces:", my_com.split(' '))

# Convert the whole string to uppercase
print("Uppercase:", my_com.upper())

# Convert the whole string to lowercase
print("Lowercase:", my_com.lower())

# Additional string methods:

# Capitalize the first character of the string
print("Capitalized:", my_com.capitalize())

# Title case the string (first letter of each word capitalized)
print("Title Case:", my_com.title())

# Swap the case of each character in the string
print("Swap Case:", my_com.swapcase())

# Check if the string is alphanumeric (contains only letters and numbers)
print("Is Alphanumeric:", my_com.isalnum())

# Check if the string is alphabetic (contains only letters)
print("Is Alphabetic:", my_com.isalpha())

# Check if the string is numeric (contains only digits)
print("Is Numeric:", my_com.isdigit())

# Check if the string is lowercase
print("Is Lowercase:", my_com.islower())

# Check if the string is uppercase
print("Is Uppercase:", my_com.isupper())

# Check if the string is a title (each word starts with an uppercase letter)
print("Is Title Case:", my_com.istitle())

# Check if the string contains only whitespace
print("Is Whitespace:", my_com.isspace())

# Strip leading and trailing whitespace
print("Stripped String:", my_com.strip())

# Justify the string to the left
print("Left Justified:", my_com.ljust(30, '-'))

# Justify the string to the right
print("Right Justified:", my_com.rjust(30, '-'))

# Center the string
print("Centered String:", my_com.center(30, '-'))

# Check if the string starts with a specified substring
print("Starts with 'This':", my_com.startswith("This"))

# Check if the string ends with a specified substring
print("Ends with 'comment ':", my_com.endswith("comment "))
