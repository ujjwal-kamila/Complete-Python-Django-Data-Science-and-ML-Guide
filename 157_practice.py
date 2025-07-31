# 157. Practice - Considering the Order of Conditions in if Statements

num = 11

if num % 3 == 0 and num % 5 == 0:
    print("Number is divisible by 3 and 5")
elif num % 3 == 0:
    print("Number is divisible only by 3")
elif num % 5 == 0:
    print("Number is divisible only by 5")
else:
    print("Number is not divisible by 3 or by 5")



