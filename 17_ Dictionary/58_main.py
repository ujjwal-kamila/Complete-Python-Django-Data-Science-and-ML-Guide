# 58.Dictionary : A set of key value pair

# examples
dict = {
    'name ':'Ujjwal',
    'age':19
}
print(dict)
print(type(dict))

# Don't matter what order is written
# let's see an example and compare them
bike1 = {
    'name' : 'Honda',
    'color': 'Blue',
    'year': 2024,
    'price':90000        
}

bike2 = {    
    'year': 2024,
    'color': 'Blue',
    'price':90000,
    'name' : 'Honda',
}
# compare them 
print(bike1==bike2)      # True
# But address ids are different bcz of two objects
print(id(bike1)==id(bike2))

# Accessing Dict
# getting values
print(bike2['color'])
print(bike2['price'])

# assign new value to key 
bike1['price']= 89000
print("Updated dictionary",bike1)

# adding new value pairs (elements)
bike1['is_new']=True
bike2['is_good']=False
print("updated is_new ",bike1)
print("Updated is_good",bike2)

# Delete specific keys using" del dict['key]"
del bike2['is_good']
print("After deleting is_good",bike2)

# accessing the key value using a variable
key_name = 'color'
bike1[key_name] = 'Black'
print("change color as Black ",bike1)




print("\n\n")


# 59. Practice - Manipulating Dictionaries
my_bike = {'brand':'Yahama','price':80_000 }
print("My Bike dict :",my_bike)
print(type(my_bike))
# length of keys 
print(len(my_bike))

# getting values of specific key using dict['key']
print(my_bike['brand'])
print(my_bike['price'])

# add some more keys
my_bike['max_speed'] = 120
print(my_bike)
print(len(my_bike))

# change/update values 
my_bike['price']=95000
print(my_bike)

# dict same as unorders key values like ex
# First car dictionary with unordered values
car1 = {
    "model": "Model S",
    "year": 2020,
    "brand": "Toyota",
    "color": "silver",

}

# Second car dictionary with unordered values
car2 = {
    "year": 2020,
    "brand": "Toyota",
    "color": "silver",
    "model": "Model S",
}
# Compare car1 and car2
print(car1==car2)