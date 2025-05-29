# 122. Practice - Short-Circuit AND Operator

def check():
    print("Function called")
    return True

print(False and check())
print(True or check())
