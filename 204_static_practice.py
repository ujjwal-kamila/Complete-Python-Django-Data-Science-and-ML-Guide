# 204. Practice - Utilizing Static Methods in Classes

class Post:
    def __init__(self, title, content, author):
        # Instance attributes
        self.title = title
        self.content = content
        self.author = author
        self.total_likes = 0

    def like(self):
        # Increase the like count 
        self.total_likes += 1

    @staticmethod
    def format_post(title, content):
        # Formats and returns a string with post details
        # Doesn't use 'self', as it's a static method
        return (
            f"Post title: {title}\n"
            f"Post content: {content}"
        )


# Create a Post object
post1 = Post("Python Tips", "Use list comprehensions!", "Ujjwal")

# Add likes 
post1.like()
post1.like()
res = post1.format_post("This is a title","This is about Python")
print(res)

# Show total likes for this post
print(f"Total Likes: {post1.total_likes}\n")

# Call the static method without creating an object
formatted_post = Post.format_post("OPPs Concept", "About Methods in OOPs")
print(formatted_post)


'''
Simple Calculator 
'''
class Calculator:
    @staticmethod
    def add(a, b):
        return a+b

    @staticmethod
    def subtract(a, b):
        return a-b

    @staticmethod
    def multiply(a, b):
        return a*b

    @staticmethod
    def divide(a,b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero.."

    @staticmethod
    def calculate(a, b, operator):
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            return "Error: Invalid number.."

        if operator == "+":
            return Calculator.add(a, b)
        elif operator == "-":
            return Calculator.subtract(a, b)
        elif operator == "*":
            return Calculator.multiply(a, b)
        elif operator == "/":
            return Calculator.divide(a, b)
        else:
            return "Error: Invalid operator..Try again"

#  user input
print("Simple Calculator")
a = input("Enter first number: ")
b = input("Enter second number: ")
op = input("Enter operator (+, -, *, /): ")

result = Calculator.calculate(a, b, op)
print(f"Result: {result}")
