# 208. Practice - Utilizing Magic Methods in Classes

class Post:
    def __init__(self, title):
        self.title = title

    def __add__(self, other):
        return f"{self.title} {other.title}"

    def __eq__(self, other):
        return self.title == other.title

# Example usage
first_post = Post("This is first post")
second_post = Post("This is second post")
third_post = Post("This is first post")

# Addition
print(first_post + second_post)  

# Equality
print(first_post == second_post)
print(first_post == third_post)
