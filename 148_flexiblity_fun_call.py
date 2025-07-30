# 148. Practice - Flexibility in Function Calls

def create_user(username, email, password):
    return f"Creating user:\nUsername: {username}\nEmail: {email}\nPassword: {password}"

user_info = {
    'username': 'ujjwal_kamila',
    'email': 'ujjwal@gmail.com',
    'password': 'securePass123',
}

created_usr = create_user(**user_info)
print(created_usr)


user2 = ['ujjwal_01', 'ujjwal@example.com', 'ujjwal@Pass456']
created_user2= create_user(*user2)
print(created_user2)
