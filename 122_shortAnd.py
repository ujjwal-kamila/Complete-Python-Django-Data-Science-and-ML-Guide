# 122. Practice - Short-Circuit AND Operator
# 'and' returns True only if both conditions are true.
def check():
    print("Function called")
    return True

print(False and check())
print(True or check())


print('Ujjwal' and 'Rudra' and 'Aashiq')
print([1,2] and {} and 'Aashiq' and True and 3.14)
'''
when 'and' finds first falsy val then it stops 
'''

