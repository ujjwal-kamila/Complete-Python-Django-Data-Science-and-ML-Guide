# 38. String Concatenation

# add to given strings 
str1 = 'Hello'
str2 = 'World'
greeting = str1 + ' ' + str2
print(greeting)

# String Formatting fstings 

str1 = 'Hello'
str2 = 'World'
greeting = f"{str1} {str2}"
print(greeting)

# Create a Data and print using f-stings 
# Sample data
name = "Ujjwal"
age = 20
occupation = "Software Developer"
address = {"city": "Kalyani", "country": "India"}

# Simple f-string usage
print(f"My name is {name}. I am {age} years old and work as a {occupation}.")
print(f"I live in {address['city']}, {address['country']}.")
