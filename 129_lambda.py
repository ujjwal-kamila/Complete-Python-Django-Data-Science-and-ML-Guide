# 129. Practice - Sorting a List using Lambda Functions

students = [
    {"name": "ujjwal", "marks": 85},
    {"name": "Amit", "marks": 95},
    {"name": "Raj", "marks": 75}
]

# def sort_marks(student):
#     return student['marks']
# students.sort(key=sort_marks)

students.sort(key= lambda student : student ['marks'])

print(students)

# Sort by length of student name
students.sort(key=lambda s: len(s['name']))
print(students)