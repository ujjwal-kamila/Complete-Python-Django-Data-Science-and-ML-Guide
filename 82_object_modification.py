# 82. Understanding Immutable Objects in Python

num1 = 10
num2 = num1        # same object

print("Id of num1",id(num1))
print("Id of num2",id(num2))

num2 = num2 + 10
print("num2 : ",num2)     #20
print("num1 : ",num1)     #10

print("Id of num1 : ",id(num1))
print("Id of num2 : ",id(num2))


# 83. Understanding Mutable Objects in Python
list1 = [1,2,4,8]
print("Id of list1",id(list1))

list2 = [1,2,4,8]
print("Id of list2",id(list2))

print("Id of list[1,2,4,8] :",id([1,2,4,8]))

# examples using dict
info = {
    'name':'Ujjwal',
    'can_vote': 'yes'
}
# coy to another dict
copy_info = info
# same Id as point to same object
print(id(info))
print(id(copy_info))

info['age'] = 19        # change the same object
print("info dict :",info)
print("Copy of info dict :",copy_info)

# 84. Strategies to Prevent Object Mutation
# avoid this mutation tusing .copy() method 

# example : same dict as uppper code
copy_of_info = info.copy()
info['age'] = 20 
print("info dict :",info)
print("Copy of info dict :",copy_of_info)       # age remain same as 19


# For nested mutable objects we use deepcopy() method 
from copy import deepcopy
details = {
    'name': 'Ujjwal Kamila',
    'age ': 20,
    'reviews':[]
}

copy_of_details = deepcopy(details)
copy_of_details['reviews'].append('Good Coder!')
print(details)
print(copy_of_details)



# 85. Practice - Creating Deep Copies of Objects
'''
Same example as previous code,,using deepcopy get different object 
using .copy ...get same object '''


