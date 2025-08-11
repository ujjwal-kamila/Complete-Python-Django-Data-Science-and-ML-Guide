# 203. Static Class Methods

class Comment:
    def __init__(self,text):
        self.text = text
        
    @staticmethod
    def merge_comments(first,second):
        return f"{first} {second}"
    
my_comment = Comment("My comment")

#  Calling the static method using the class name
comment_1 = Comment.merge_comments("Thanks!", "Excellent")
print(comment_1)

# Calling the static method using an object
comment_2 = my_comment.merge_comments("Great!", "Ok")
print(comment_2)
