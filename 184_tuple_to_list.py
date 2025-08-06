# 184. Practice - Converting Tuples to Lists

'''
my_list = [item for item in my_tuple]
'''

# example
coordinates = (480,720,1080)

coordinate_list = [coordinate *2 for coordinate in coordinates]
print(coordinate_list)


# filter even nmbers from tuple into list
nums = (10, 15, 20, 25, 30)
even_nums = [x for x in nums if x % 2 == 0]

print(even_nums)

# Convert tuple of strings to uppercase list
names = ("ujjwal", "raj", "aashiq")
upper_names = [name.upper() for name in names]

print(upper_names)

