# 201. Instance vs Class Methods

# instance methods
class Car:
    def __init__(self, brand):
        self.brand = brand   # instance attribute

    def show_brand(self):   # instance method
        print(f"Car brand is {self.brand}")

# Create object
car1 = Car("BMW ")
car1.show_brand()   
Car.show_brand(car1) 



# sample example
class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.votes_qty += 1

first_comment = Comment("First comment")

print(first_comment.text)         
print(first_comment.votes_qty)      

first_comment.upvote()
print(first_comment.votes_qty)     

first_comment.upvote()
print(first_comment.votes_qty)     

print(isinstance(first_comment, Comment))  # True
print(type(first_comment) == Comment)      # True
print(isinstance(first_comment, object))   # True
