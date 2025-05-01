# 90. Practice - Using Mutable and Immutable Objects as Function Arguments
def print_fav_fruits (person,fruits):
    # fruits_cpy = fruits.copy()
    print(id(fruits))
    fruits.pop()
    for fruit in fruits :
        print(f"{person} likes {fruit}")
    
name = 'Ujjwal'
fruits = ['Apples','Oranges','Bananas']

# fun call 
print_fav_fruits(name , fruits)
# if mutable the list 
print(id(fruits))   #same object


# 91. Practice - Mandatory and Optional Positional Arguments

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# Calling the function
greet("Ujjwal", 20)  # Correct
# greet("Ujjwal")      # TypeError

# another type 
def greet(name, age=18):  # 'age' is an optional
    print(f"Hello, {name}! You are {age} years old.")

# Calling the function
greet("Ujjwal", 21)  # Hello, Ujjwal! You are 21 years old.
greet("Ujjwal")      # Hello, Ujjwal! You are 18 years old. (uses default value)


# ---------- TASK -----------
'''
1.Create a merge_lists_to_dict function
2.The function must have two parameters 
3.The function should combine two lists using the built in zip function 
4.Conver a zip object to a dictionary and return it from the function 
5.Call a function by passing it two lists as arguments 
6.Output the result of the function call to the terminal '''

# Create a merge_lists_to_dict function
def merge_lists_to_dict(list1,list2):
    zip_res= zip(list1,list2)
    result = dict(zip_res)
    return result

# Create two lists as Key Value 
l1 = ["name",'branch','roll',"age","Is_adult"]
l2 = ["Ujjwal","CSE",22033,20,True]
res = merge_lists_to_dict(l1,l2)

# Output of result
print("Combine Dict is :",res)



# 93. Function Arguments
# can add more arguments using .args in function parameter
def sum_nums(*args):
    print(args)
    print(type(args))
    return sum(args)

print(sum_nums(5,6,7))

# Create a fun as two args that person name ans post numbers
def fun_post (name,posts_num):
    info =print(f"{name} wrote {posts_num} posts in Linkedin")
    return info 
fun_post("Ujjwal",5)


