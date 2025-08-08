# 200. Practice - Incorporating Own Instance Attributes with the __init__ Method

# better approach to use init method
class User:
    def __init__(self, username, email):
        # Instance attributes automatically set at creation
        self.username = username
        self.email = email

    def info(self):
        print(f"User {self.username} has email {self.email}")

# Create object and set attributes in one step
first_user = User('ujjwal123', 'ujjwal@ujjwal.com')
other_user = User('raj123', 'raj@11.com')

# call method
first_user.info()
other_user.info()

# Modify email later
first_user.email = 'makaut@gamil.com'

# Show updated info
first_user.info()

# show the object dictionary 
print(first_user.__dict__)