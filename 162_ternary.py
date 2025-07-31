# 162. Ternary Operator

# <variable> = <value_if_true> if <condition> else <value_if_false>

# simple example 
age = 20
canVote = "Major " if age>18 else  "Minor"
print(canVote)

# simple even odd
num = 7
print("Even") if num % 2 == 0 else print("Odd") 


# multiple condition 
marks = 85
grade = "A" if marks > 90 else "B" if marks > 80 else "C"
print(grade)


# is int or not
number = 3.14
print("Is int") if type(number) is int else print("Not integer")

# check stock avilable or not 
products_qnty = 0
print("Avilable") if products_qnty > 0 else print("Out of Stock! ")