# 123. Practice - Combining OR and AND Operators

#  Question: Is the number negative or greater than 100?

# num = int(input("Enter a number: "))
# if num < 0 or num > 100:
#     print("Out of range")
# else:
#     print("In range")

# leap year cheking
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap year")
else:
    print("Not a leap year")


# login system using otp 
username = input("Enter username: ")
password = input("Enter password: ")
otp = input("Enter OTP: ")

if username == "admin" and (password == "Adminpass@123" or otp == "1022"):
    print("Login successful")
else:
    print("Login failed")
