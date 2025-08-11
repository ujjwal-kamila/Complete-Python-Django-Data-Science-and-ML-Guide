# 206. Practice - Working with Class Attributes

# user login count
class User:
    # Class attribute to count logins
    total_logged_in_users = 0  

    def __init__(self, username):
        self.username = username

    def login(self):
        User.total_logged_in_users += 1
        print(f"{self.username} logged in.")

# Example usage
user1 = User("ujjwal")
user2 = User("aashiq")
user3 = User("rudra")

user1.login()
print("Total logged in users:", User.total_logged_in_users)  

user2.login()
print("Total logged in users:", User.total_logged_in_users)  

user3.login()
print("Total logged in users:", User.total_logged_in_users)  
