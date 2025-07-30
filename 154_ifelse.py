# 154. The if-else Statement
'''
# if Statement Format: ->
if condition:
    # code runs if condition is True

'''
temp = 39

if temp > 30:
    print("It's a hot day.")


'''
# if-else Statement Format: ->
if condition:
    # code runs if condition is True
else:
    # code runs if condition is False

'''
# even odd check 
number = 17

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")



'''
# if-elif-else Statement Format: ->

if condition1:
    # runs if condition1 is True
elif condition2:
    # runs if condition1 is False and condition2 is True
else:
    # runs if all above conditions are False
'''
def check_eligibility(age, is_citizen):
    if age >= 18 and is_citizen:
        print(" Can vote")
    elif not is_citizen:
        print(" Not a citizen")
    else:
        print(" Underage")

check_eligibility(17, True)
check_eligibility(25, False)

# not with if

nums = [ 1,32,5,7,8,15]
if 10 not in nums:
    print("True")


'''
TErnary :->
value_if_true if condition else value_if_false
'''
marks = 45
result = "Pass" if marks >= 50 else "Fail"
print(result)

#check postivve using ternary
x = -1
value = "postive" if x > 0 else "Negative" if x < 0 else "Zero"
print(f"{x} is :",value)
