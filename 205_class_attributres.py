# 205. Class Attributes

# Counting total instances created
class Comment:
    total_comments = 0  # Class attribute

    def __init__(self, text):
        self.text = text           
        self.votes_qty = 0       
        Comment.total_comments += 1

# Creating objects
first_comment = Comment("First comment")
print(Comment.total_comments)  

second_comment = Comment("Second comment")
print(Comment.total_comments)  


# tracking students in a class
class Student:
    total_students = 0  # Class attribute

    def __init__(self, name):
        self.name = name
        Student.total_students += 1

student1 = Student("Raj")
student2 = Student("Roni")


print(Student.total_students) 
