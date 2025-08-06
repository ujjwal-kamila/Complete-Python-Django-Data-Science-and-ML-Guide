# 179. For-In Expression
# for variable in iterable:
#     # code block to execute

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


word = "Hello World"

for letter in word:
    print(letter)

# Loop using range()
for i in range(5):  
    print(i)

# over dict
person = {"name": "Ujjwal", "age": 21}

for key in person:
    print(key, ":", person[key])
