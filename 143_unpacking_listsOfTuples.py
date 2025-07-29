# 143. Practice - Unpacking a List of Tuples

user_credits = [
    ("user1","pass_one1"),
    ("user2","pass_two2"),
    ("user3","pass_three3")
]

# unpack 
user1,user2,user3 = user_credits
# each user as a tuple
print(user1)
print(user2)
print(user3)

# do the 3 tuples in 3diff variables
# Unpacking Each Tuple into Username and Password
user1_username, user1_pass = user1
user2_username, user2_pass = user2
user3_username, user3_pass = user3


print(user1_username,user1_pass)
print(user2_username,user2_pass)
print(user3_username,user3_pass)