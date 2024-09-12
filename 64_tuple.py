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
