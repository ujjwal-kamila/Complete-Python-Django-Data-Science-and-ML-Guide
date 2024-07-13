# 36. Practice - String Manipulation & Escape Characters 

# create a str 
long_str = "It\'s a Rainy day today"
# We have to use escape characters '\' like :
long_str = 'It\'s a Rainy day today'

# also to split a str we have to put a backslash '\'
long_str1 = "Hii "\
    "This is "\
        "a very long "\
            "string."
print(long_str1)

print(long_str)
print(type(long_str))
print(type(long_str)== str)
print(id(long_str))

# We cannot write more than 79 characters in one line so we use multiline
mul_str = "This is a very, very,"\
    " very, very,"\
    " very, very,"\
    " very, very,"\
    " very, very,"\
    " very, very,"\
    " very, very,"\
    " very, very,"\
    " very, very,"\
    " very, very,"\
        "long string."
    
print(mul_str)

mul_str1 = '''
    This 
    is 
    a 
    very, 
    very ,very,
    very, 
    very ,very, 
    very, very ,
    very, very ,
    very ,very ,
    very ,very ,
    very ,very, 
    very, very
    long string'''
    
print(mul_str1)