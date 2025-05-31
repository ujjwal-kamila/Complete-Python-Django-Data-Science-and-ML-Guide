# 126. The del Statement

'''
del : does not return anything. It just removes the reference.
'''

# syntax like 
# del variable
# del list[index]
# del list[start:end]
# del dict[key]

# examples : list
fruits = ['apple', 'banana', 'cherry', 'date','mango']
del fruits[1]  # deletes 1st index
print(fruits) 

del fruits[1:3]  # delets 1st to 3rd index
print(fruits)


# examples : dict
student = {'name': 'Ujjwal', 'age': 20, 'dept': 'CSE'}
del student['age']
print(student)  # deleted age key

# Deleting a variable 
input_var = 100
del input_var
# print(x)    # Error: x is not defined


