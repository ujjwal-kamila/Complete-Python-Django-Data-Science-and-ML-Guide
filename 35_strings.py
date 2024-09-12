# 35. Strings in Python

#  Use double quotes or single quotes for str "Hii " or  'Hii'

my_name = 'Ujjwal Kamila'
print("My name is : ",my_name)
print(id(my_name))
print(type(my_name))
# let's see another examples

greeting = "Hello World!" 
print("greeting")

# '''triple quotes or double Multiline strings 


str = '''Hii
this is basics of python
This is a multi line string'''

str1 = """
Hii
this 
is
basics 
of 
strings 
"""

print(str)


# str concatination "[start:end:stepvalue]""
print(my_name[0])
print(my_name[0:4])  # means  upto 4th position


# Original string
my_name = 'Ujjwal Kamila'

# Convert to uppercase
upper_name = my_name.upper()
print(f"Uppercase: {upper_name}")

# Replace 'Kamila' with 'Smith'
replaced_name = my_name.replace('Kamila', 'None')
print(f"Replaced: {replaced_name}")

# Count occurrences of 'a'
count_a = my_name.count('a')
print(f"Count of 'a': {count_a}")

# Find the index of 'Kamila'
index_kamila = my_name.index('Kamila')
print(f"Index of 'Kamila': {index_kamila}")

# Capitalize the string
capitalized_name = my_name.capitalize()
print(f"Capitalized: {capitalized_name}")

# Convert to lowercase
lower_name = my_name.lower()
print(f"Lowercase: {lower_name}")
