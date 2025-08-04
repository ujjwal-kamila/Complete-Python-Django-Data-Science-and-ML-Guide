# 176. Practice - Using break Statements in While and For-In Loops

user_pass = 'admin@123'
password =''

while password != user_pass:
    print("Enter 'quit' to exit from login ")
    password= input("Please Enter your password : ")
    if password == 'quit':
        print("Quit...")
        break

if password == user_pass:
    print("Login Sucessful")
else:
    print("Login Failed")


# using of break 
my_list = [10,2,5,78,9,0]

for num in my_list:
    if num == 5:
        break
    print(num)