# 120. Logical Operators

# and	->True if both are True
# or	-> True if at least one True
# not	-> Reverses True/False

# Example of 'and' operator
x = 5
y = 10

# Both True
if x > 0 and y > 0:
    print("Both x and y are positive.")

# Example of 'or' operator
a = -3
b = 7

# At least one condition must be True
if a > 0 or b > 0:
    print("At least one number is positive.")

# Example of 'not' operator
is_raining = False

#  not False means -> True
if not is_raining:
    print("You can go outside.")


'''
Check if a number is between two values
'''
def is_bet_check(num,low,high):
    # return num in range(low,high+1)
    if num>=low and num<=high:
        return True
    else:
        return False
    
res= is_bet_check(10,9,15)
print("this is :",res)