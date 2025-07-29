# 144. Practice - Unpacking Remaining Elements

person = ("Alice", 25)
# Unpacking ✅ Works 
name, age = person     
# ❌ Error: too many variables               
# name, age, place = person
# ✅ Correct even if extra variables not available : * to Catch Extra Items
name, age, *other = person

print(name)
print(age)
# Empty value
print(other)


# * is used to capture remaining elements in unpacking
# examples
grades = (80,75,69,20,91)
first, *middle , last = grades

print(first)
print(middle) 
print(last)

first,second,*remaining = grades
print(first)
print(second)
print(remaining)