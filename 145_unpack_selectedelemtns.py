# 145. Practice - Unpacking Selected Elements

# ingnore the rest using _ or *

# example: 1
values = [10, 20, 30, 40, 50]

# * _ grabs the middle values
first, *_, last = values

print("First:", first)   
print("Last:", last)     

# example: 2
person = ("ujjwal", 25, "Engineer", "Kalyani")

# *rest for the remaining
name, age, *rest = person

print("Name:", name)      
print("Age:", age)        
print("Rest:", rest)


# example: 3
data = (1, 2, 3, 4, 5)

# _ uses to skip & *_ for remaining values 
first, _, third, *_ = data

print("First:", first)  
print("Third:", third)

