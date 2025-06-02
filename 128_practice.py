# 128. Practice - Returning Lambda Functions from Functions

def multiply(multiplier):
    return lambda  x : x * multiplier

multiply_by3 = multiply(3)
print(multiply_by3(10))

# add 
add = lambda a, b: a + b
print(add(5, 3)) 

# square
square = lambda x: x * x
print(square(4)) 

# Even Odd check 
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(5))  #  Odd


# use map to square a list 
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, nums))
print(squares)

# sort dict using key and lambda
students = [
    {"name": "Rohan", "score": 85},
    {"name": "Amit", "score": 95},
    {"name": "Raj", "score": 75}
]

sorted_by_score = sorted(students, key=lambda x: x["score"])
print(sorted_by_score)


# Find longest string
words = ["pen", "pencil", "eraser", "ink"]
longest = max(words, key=lambda x: len(x))
print(longest)  
