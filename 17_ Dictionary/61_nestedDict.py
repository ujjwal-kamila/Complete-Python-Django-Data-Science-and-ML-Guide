# 61. Other Operations with Dictionaries
# nested dictionary
names = {
    'student1':{
        'name':'David',
        'age':16,
        'result':'pass'
    },
    'student2':{
        'name':'Alice',
        'age':16,
        'result':'fail'
    },
    # more
}

# accessing nested dict using dict[][]
print("Name of Student 1 :",names['student1']['name'])
print("Result of Student 1 :",names['student1']['result'])
print("Name of Student 2 :",names['student2']['name'])
print("age of Student 2 :",names['student1']['age'])

# Create dict using variables 
name = 'Mr.Bean'
age = 69
education = 'B.Tech'
work = 'Comedy Cartoon'

mrBean_details = {
    'Name':name,
    'Age': age,
    'Education':education,
    'Work': work
}
print(mrBean_details)

# lenth of the dict
print(len(mrBean_details))

# Delete any key
del mrBean_details['Education']
print("After Deletion :",mrBean_details)