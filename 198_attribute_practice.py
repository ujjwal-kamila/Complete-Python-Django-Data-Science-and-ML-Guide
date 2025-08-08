# 198. Practice - Adding Instance Attributes through Dot Notation

# Define a class named User
class User:
    def info(self):
        # print(self.__dict__)  # Uncomment to view all instance variables as a dictionary
        print(f"User : {self.username} has email {self.email}")

# Create an object 
first_user = User()

# Assign attributes 
first_user.username = 'ujjwal'
first_user.email = 'ujjwal@gmail.com'

# Call the info method
first_user.info()

