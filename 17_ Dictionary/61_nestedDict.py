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

# if key not in dict then keyerror
# check the key is avilable or not(None)
print(mrBean_details.get('salary'))

# get specific details 
print(mrBean_details.get('Age'))
print(mrBean_details.get('Name'))
print(mrBean_details.get('Work'))
print(mrBean_details.get('salary',0))


# Magic attribute __doc__
# my_dict  = { }
# print(my_dict.__doc__)



# more examples of nested dict
students = {
    "student1": {
        "name": "John",
        "age": 20,
        "roll": "CSE101",
        "branch": "CSE",
        "marks": {
            "math": 85,
            "physics": 90,
            "chemistry": 78
        }
    },
    "student2": {
        "name": "Emma",
        "age": 21,
        "roll": "IT202",
        "branch": "IT",
        "marks": {
            "math": 88,
            "physics": 92,
            "chemistry": 81
        }
    },
    "student3": {
        "name": "Michael",
        "age": 22,
        "roll": "ECE303",
        "branch": "ECE",
        "marks": {
            "math": 82,
            "physics": 87,
            "chemistry": 79
        }
    },
    "student4": {
        "name": "Sophia",
        "age": 23,
        "roll": "EE404",
        "branch": "EE",
        "marks": {
            "math": 90,
            "physics": 85,
            "chemistry": 88
        }
    }
}

# Accessing a value (e.g., Emma's physics mark)
print("Emma's Physics Mark:", students["student2"]["marks"]["physics"])

# Changing a value (e.g., update Michael's age)
students["student3"]["age"] = 23
print(students)

# # Printing the modified dictionary
# print("\nModified Students Dictionary:")
# for student, details in students.items():
#     print(f"\n{student}:")
#     for key, value in details.items():
#         if isinstance(value, dict):
#             print(f"  {key}:")
#             for subject, mark in value.items():
#                 print(f"    {subject}: {mark}")
#         else:
#             print(f"  {key}: {value}")
