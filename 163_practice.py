# 163. Practice - Utilizing the Ternary Operator

user_active = True

status = print("Active") if user_active else print("Inactive")

# using fun 
def check_user_status(is_active):
    user_status = "Active" if is_active else "Inactive"
    return user_status

user_active = False
status = check_user_status(user_active)
print(status)


# check is a char is voewl or not 
ch = input("Enter a Character : ")
print("Vowel" if ch.lower() in 'aeiou' else "Not vowel")
