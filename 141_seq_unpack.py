# 141. Sequence Unpacking :Sequence unpacking allows you to assign multiple values from a sequence (like list, tuple, string) to multiple variables in a single line.


'''
Unpacking menas extract values and assign them to variables
only ordered type can do unpacking not unordered tpyes as dict 
'''

a, b, c = [1, 2, 3]
print(a)  
print(b) 
print(c)


# Tuple Unpacking
x, y = (10, 20)
print(x) 
print(y)


ch1,ch2,*ch3_6 = 'Python'
print(ch1,ch2)   # P y


# using * when unpacking 
my_fruits = [ 'apple','banana','cherry']
my_apple , *remain_fruits = my_fruits
print(my_apple)
print(remain_fruits)
print(type(remain_fruits))


# unpacking dict using keyword args
user = {
    'name': 'Ujjwall',
    'commits_today': 5,
}

def user_info(name,commits_today=0):
    if not commits_today:
        return f"{name} has not commits today"
    
    return f"{name} has {commits_today} commits today"

# unpacking using ** 
print(user_info(**user))

# unpacking any list to positional arguments
user = ['Ujjwal',10,True]

def user_info(name,commits_today=0):
    if not commits_today:
        return f"{name} has not commits today"
    
    return f"{name} has {commits_today} commits today"

# unpacking list  using * whne only required elemets in list 
# print(user_info(*user))
# Correct call using slicing when more elements in list 
print(user_info(*user[:2]))