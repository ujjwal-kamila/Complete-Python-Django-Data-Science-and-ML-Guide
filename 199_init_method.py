# 199. Adding Instance Attributes using the __init__ Method

# Define a Student class
class Student:
    def __init__(self, name, age, grade):
        # Instance attributes
        self.name = name
        self.age = age
        self.grade = grade

    # Method 
    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, Grade: {self.grade}")

# Create objects
student1 = Student("Aashiq", 23, "A")
student2 = Student("Ujjwal", 21, "A+")

# Call methods
student1.introduce()
student2.introduce()

# Print object dictionary 
# print(student1.__dict__) 
#  available attributes/methods 
# print(dir(student1))      


# Another example: Comment system
class Comment:
    def __init__(self, text):
        self.text = text         
        self.votes_qnty = 0 

    def upvote(self):
        self.votes_qnty += 1 

# Create Comment object
first_comment = Comment("First Comment")

# Upvote and print result
first_comment.upvote()
print(f"Comment: '{first_comment.text}', Votes: {first_comment.votes_qnty}")
