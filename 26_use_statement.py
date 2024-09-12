# 26. Practice - Using Statements : perform some actions

a = 20 # sample of statement

# import functions 
import datetime

y = datetime.MAXYEAR
print("Maximum years is :",y)


if 10 > 9 :
    print("True")    


## TASK : 
# crete any function and use inside of it a return statement
def square(num):
    res = num ** 2 
    return res

num= 5
square_val = square(num)
print(f"The square value of {num} is:",square_val)
