# 30. Types and Data Structures Overview

# Immutable Objects : cannot be changed after they are created
'''
Types of Immutable objects :
1.Integers
2.Floats
3.Strings
4.Tuples
5.Boolean
6.None
'''
print("For Immutable Objects")

# Immutable Objects
# Integers 
x = 10
print("Original x:", x, "Original Address:", id(x))
x = x + 1
# address changes for new int x
print("Modified x:", x, "Modified Address:", id(x))


# String
s = "hello"
print("Original s:", s, "Original Address:", id(s))
s = s + " world"
# address changes for new string s
print("Modified s:", s, "Modified Address:", id(s))


# Tuple
t = (1, 2, 3)
print("Original t:", t, "Original Address:", id(t))
t = t + (4,)
# address changes for new Tuple t
print("Modified t:", t, "Modified Address:", id(t))

# Mutable Objects : 
'''Types of Immutable objects :
1.Lists
2.Dictionaries
3.Sets
4. User defined classes
'''


# Mutable Object
print("For Mutable Objects")

# List
lst = [1, 2, 3]
print("Original lst:", lst, "Original Address:", id(lst))
lst.append(4)
# new adress is also same as previous address
print("Modified lst:", lst, "Modified Address:", id(lst))


# Dictionary
d = {"a": 1, "b": 2}
print("Original d:", d, "Original Address:", id(d))
d["c"] = 3
# new address is also same as previous address
print("Modified d:", d, "Modified Address:", id(d))


# Set
s = {1, 2, 3}
print("Original s:", s, "Original Address:", id(s))
s.add(4)
# new address is also same as previous address
print("Modified s:", s, "Modified Address:", id(s))


