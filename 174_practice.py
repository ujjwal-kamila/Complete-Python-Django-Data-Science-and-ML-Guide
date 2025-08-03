# 174. Practice - Utilizing the While Loop


username = ""
while not username:
    entered_username = input("Please enter your username: ")
    if len(entered_username) >= 3:
        username = entered_username
    else:
        print("Username must be at least 3 characters long. Please try again.")

print(f"Welcome, {username}")


# using sleep fun timer
import time

seconds_qty = 10

while seconds_qty > 0:
    print(f"Timer: {seconds_qty} seconds remaining...")
    seconds_qty -= 1
    time.sleep(1)

print("Timer is up!")