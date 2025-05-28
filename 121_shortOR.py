# 121. Practice - Short-Circuit OR Operator

# short circuit OR : means check the first condition if True then stops checking
def check():
    print("Function called")
    return True

result = True or check()   #True is enough to satisfy or
print("Result:", result)  