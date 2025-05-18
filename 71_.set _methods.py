# 71. Practice - Usage of the Set Methods

# Coping set and add elements to it 
my_set = {1,47,7,3}
other_set = {10,50,34,24}

# copy other set to another set
copy_set = other_set.copy()
copy_set.add(1000)
print("Copy set of other set with adding 1000 :",copy_set)
print("Other set ",other_set)

# checking subset and superset
print(other_set.issubset(copy_set))
print(copy_set.issuperset(other_set))


# 72. Practice - Calculating Symbmetric Difference of Sets

a = {'a','b','c','d'}
b = {'f','g','c','h'}
print(a.symmetric_difference(b))

# solve using union(and) intersaction(or)
print((a | b ) - (a & b))

''' 
73. TASK - Working with Sets
'''

# 1.Create a set of several elements of the int type
integer_set = {501,502,503,504,592}

# 2.add another element to it 
integer_set.add(594)
integer_set.add(494)

# 3.Create another set with several elements , some of the which should be the same as in the first
another_int_set = {502,592,301,392,594,504}

# 4.Find the common elements in two sets and place them is a new set
common_set = integer_set.intersection(another_int_set)
print("Set of Common elements :",common_set)

# 5.Convert the resulting set to a list and print the list 
list_of_set = list(common_set)
print("List of the Common set :",list_of_set)
