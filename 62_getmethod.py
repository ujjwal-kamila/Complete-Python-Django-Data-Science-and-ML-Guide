# 62. Practice - Using the get() Method for Dictionaries

my_laptop = {
    'brand': 'Lenovo',
    'color': 'white',
    'price': '64,000'
}

# Key 'ram' does not exist, so it returns None
print(my_laptop.get('ram'))

# Key 'ram' does not exist, so it returns the default value '8GB'
print(my_laptop.get('ram', '8GB'))  

# Key 'color' exists, so it returns the value 'white'
print(my_laptop.get('color'))  # Output: white

# Key 'price' exists, so it returns the value '64,000'
print(my_laptop.get('price', '70,000'))


#'''
# 63. Practice - Converting Other Types to a Dictionary
#'''

# str to dict 
str = 'Ujjwal'
# sample_dict = dict(str) # error for one 

# list to dict 
# create a list of list to means as key value
my_list = [['A',100],['B',1000]]
print(dict(my_list))

# same we can do as a tuple like [('u',1),('k',3)]
sample_tuple = (('a',5),('b',8))
print(dict(sample_tuple))

'''
..............Task..................
'''

# 1. Create an empty dictionary
user = {}

# 2, Three times ask the user ti enter the name of the ke first and the enter a value for this key..There should be a total of 6 text input requests 

key1 = input("Enter the name of 1st key : ")
value1 = input("Enter the evalue of 1st key : ")

key2 = input("Enter the name of 2nd key : ")
value2 = input("Enter the evalue of 1st key : ")

key3 = input("Enter the name of 3rd key : ")
value3 = input("Enter the evalue of 1st key : ")

# when reciveing data from the user , add keys with values to the dict according to the what the user entered 
user = {
    key1: value1,
    key2: value2,
    key3: value3
}

'''
Can do also with assigning key values as like below 
'''
# user [key1] = value1
# user [key2]= value2
# user [key3]=value3


# print the result dict in terminal
result = user
print("User Dictionary : ",result)