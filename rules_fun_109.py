# /109. Rules for Working with Functions
'''
1.name functions bases on the tasks that do
2.the name of the fun should begin with the verb(action word)
3.one fun should do one task
4.Not recommneded to change external variables 
'''

# Exmaple : 1
def calculate_sum(a, b):
    return a + b


# Example :2
def print_message(msg):
    print(msg)
    
# Example: 3
def get_user_name():
    return input("Enter your name: ")

# Example : 4
def add_one(num):
    return num + 1

x = 5  #external variable
y = add_one(x)  # y becomes 6 x remain same
