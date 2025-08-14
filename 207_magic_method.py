# 207. Magic Methods in Classes

class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.votes_qty += 1

    def __add__(self, other):
        return (f"{self.text} {other.text}", self.votes_qty + other.votes_qty)

# Usage:
first_comment = Comment("First comment")
first_comment.upvote()

second_comment = Comment("Second comment")
second_comment.upvote()

print(first_comment + second_comment)
