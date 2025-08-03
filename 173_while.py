# 173. While Loop

'''
Syntax:

while condition: 
    # code block executed if condition # true 
'''

while True:
    ans = input("Enter yes or no :")
    if ans == 'no':
        break


# Guess numbers 
import random 
ran_num = random.randint(1,5)
while True:
    num =int(input("Guess the number from 1 to 5 :"))
    if num != ran_num:
        print("Try again...")
    print("Congratulations!.",ran_num)
    break

