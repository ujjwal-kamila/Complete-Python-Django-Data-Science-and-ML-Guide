# 65. Tuples : immutable , can't be changes 

# examples 
user_ip = (100,180,1790,6045,7982,2253)
user_inp = (True,10.557,False,190,'Hello World')

# Types
print(type(user_ip))
print(type(user_inp))


# order of elemets make the tuple different
# examples
fruits = ('apple','grapes','mango')
fruits1  =  ('mango','apple','grapes')
print(fruits ==fruits1)    # False

# checking ids 
print(id(fruits))
print(id(fruits1))

# Compare ids 
print(id(fruits)==id(fruits1))      # False 

# Access and assign 
tup_id = (141,299,456,366)
# also get neg index using [] notation 
print(tup_id[0])
# print(tup_id[5]) # index out of bound
print(tup_id[::-1]) # also reverse

# cannot modified tuple : delet or assignn new elemets 
# tup_id[0]= 1       #Error
# del tup_id[1]     #Error

# Tuples of dictionaries ( {} )
users = (
    {
        'id' : 102,
        'name': 'Alice'
    },
    {
        'id' : 105,
        'name': 'Bob' 
    }
)
print(type(users))

print(users[1]['id'])   # 105

# Can modifies tuple dictionaries 
users[1]['id'] = 200   

print(users[1]['id'])  # 200


# Create tuples using variables 
var1 = True
var2 = False
var3 = 98.4
var4 = 1000
var5 = 'Hello'
var6 = '$'

tup_vars = (var1,var3,var2,var4,var5,var6)
print("Tuple using variables :",tup_vars)

# magic Methods using tuples 
first_ids = (100,156,587,942,397,349)
next_ids = (3548,2126,133,1639)
# using add  + operator , __add__ method is called
print("All ids are :",first_ids+next_ids)


# Two Methods in Tuples 
'''
Count : counting the repeated one
index : find index of the specific elements 
'''

post_id = (10,80,10,88,10,77,99,10)
print("Count of 10 : ",post_id.count(10))
print("index if 10 is : ",post_id.index(10))
print("index if 88 is : ",post_id.index(88))


# Tuple to list conversion 
tup_fruits  =  ('mango','apple','grapes')
list_of_tup = list(tup_fruits)
print(list_of_tup)


# 66. Practice - Tuples Manipulation

resolution = (1920,1080)
#Crating list from it 
res_list = list(resolution)
print(type(res_list))
print(res_list)

# adding two tuples to create a new tuple
data = (True,'Realme',16000)
res = (1980,1080)
screen_data = data + res 
print(screen_data)

# Accessing datas by index
print(data[0])
print(data[-1])
print(res[0])

# Length of Tuple
print(len(data))