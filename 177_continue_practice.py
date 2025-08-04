# 177. Practice - Using continue and break Statements in While Loops

saved_usernames = ['raj321', 'ujjwal86','aasiq033']

while True:
    user_name = input("Please enter desired username : ")

    if user_name in saved_usernames:
        print("Username alredy taken..Try again")
        continue
    
    saved_usernames.append(user_name)
    break

print("User Registration complete! ")
print(saved_usernames)