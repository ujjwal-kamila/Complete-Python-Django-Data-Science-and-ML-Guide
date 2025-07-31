# 167. Loops Basics

# wihout using loops
# List
my_list = [1, 3, 7]
print("List without loop:", my_list[0], my_list[1], my_list[2])

# Tuple
my_tuple = ('X', 'Y', 'Z')
print("Tuple without loop:", my_tuple[0], my_tuple[1], my_tuple[2])

# Dictionary
my_dict = {'x':10, 'y': 3}
print("Dict without loop:", list(my_dict.items())[0], list(my_dict.items())[1])

# Set (convert to list since sets are unordered)
my_set = {'apple', 'banana'}
set_list = list(my_set)
print("Set without loop:", set_list[0], set_list[1])

# String
my_str = "Hii"
print("String without loop:", my_str[0], my_str[1], my_str[2])

'''
Using Loops
'''
# List
print("\nList with loop:")
for item in my_list:
    print(item)

# Tuple
print("\nTuple with loop:")
for item in my_tuple:
    print(item)

# Dictionary
print("\nDict with loop:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Set
print("\nSet with loop:")
for item in my_set:
    print(item)

# String
print("\nString with loop:")
for ch in my_str:
    print(ch)
