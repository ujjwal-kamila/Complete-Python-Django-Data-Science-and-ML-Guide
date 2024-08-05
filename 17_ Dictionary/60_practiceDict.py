# 60. Practice - Dictionary Methods
car = {
    "year": 204,
    "brand": "Toyota",
    "color": "Blue",
    "model": "Model S",
}

# Display keys using .keys()
keys = car.keys()
print(keys)
print(type(keys))

# using loop
for key in car.keys():
    print(key,end='  ')
    
# display values using .value()  
print("\nvalues are : ",car.values())
# also get using loop also 
print("Values are : ",end= ' ')
for value in car.values():
    print(value,end ='  ')
    
# convert dict keys to list using list[keys]
list_keys = list(keys)
print("\nlist of Keys are : ",list_keys)

# Dict items using dict.items() 
# Get tuples using dict.items()
print("As Tuple :",car.items())

# Create a copy of the dictionary
my_bike = {
    'brand' : 'Custom',
    'max speed':120,
    'price': 90000
}

# same object modified both
other_bike = my_bike
other_bike['color'] = 'Blue'
print("My bike :",my_bike)
print("Other bike :",other_bike)

# Create new object from existing one using .copy()
other_bike = my_bike.copy()
other_bike['color'] = 'Red'
print("\nMy bike :",my_bike)
print("Other bike :",other_bike)



