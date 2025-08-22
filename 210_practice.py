# 210. Practice - Extending Classes


class User:
    def __init__(self, username, email):
        # store username and email
        self.username = username   
        self.email = email        

# AdminUser inherits from User
class AdminUser(User):            
    def __init__(self, username, email, role):
        # call parent constructor
        super().__init__(username, email)  
        self.role = role           
        self.is_admin = True

my_admin = AdminUser('admin123', 'admin@admin.com', 'Administrator')

# prints object info
print(my_admin)   
# prints class type                       
print(type(my_admin))                     
print(isinstance(my_admin, AdminUser))    
print(isinstance(my_admin, User))         
print(isinstance(my_admin, object))

# prints attributes as dict
print(my_admin.__dict__)    

my_user = User('ujjwal01','ujjwal01@gmail.com')          
print(my_user.__dict__)    

# subclasses of User
print(User.__subclasses__())              
