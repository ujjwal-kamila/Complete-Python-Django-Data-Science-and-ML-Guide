# 180. List, Set, and Dictionary Comprehensions

# List comprehension
all_nums = [3.14,1,-5,34,8,0,-20]

# get the positive values using abs(-1) = 1
absolute_num = [abs(num) for num in all_nums]

print("Absolute nums :",absolute_num)
print("All nums :",all_nums)


# filter a list using for  loop 
sample_list = [0,-1,20,-4,5,-30]
positive_nums = []
for num in sample_list:
    if num>0 :
        positive_nums.append(num)
print("Positive nums :",positive_nums)
print("All nums :",sample_list)

# filter same list using for in mehtod
pos_nums = [num for num in sample_list if num>0]
print("Positive nums :",pos_nums)

# Set comprehension
# Create a new set using for in loop 
my_set = {1,20,40}
new_set = set()
for val in my_set:
    new_set.add(val+1 )

print("old set is",my_set)
print("new set is",new_set)

# can Use unpacking
my_set = {1, 20, 40}
new_set = {*my_set}
print("new set is",new_set)
print("old set is",my_set)


# Use set comprehension 
my_set = {1, 20, 40}
new_set = {val*val for val in my_set}
print("new set is",new_set)
print("old set is",my_set)



# dict comprehension
# using loop 
scores = {
    'a': 45,
    'b': 90,
    'c':10
}

new_scores = {}

for key,val in scores.items():
    new_scores[key]=val*5
    
print("Old score :",scores)
print("New score :",new_scores)

# using dict comprehension
updated_score= {
    key:val *10 for key,val in scores.items()
}
print("Old score :",scores)
print("New score :",updated_score)
