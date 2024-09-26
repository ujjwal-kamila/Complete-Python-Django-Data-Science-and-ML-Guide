# 67. Sets : unordered sequence of elements.
'''
Contain unique elements
Object of same type (diffenet type also acceptable)
'''
# examples 
# empty set -> set()  "{}is an empty dict" 
set1 = set()
print(type(set1))
print(set)

fruits = {'apple','mango','orange','grapes'}
ids = {101,201,302,503,492}
inputs = {True,'hi','😊',3.14}
print(type(inputs))
# lenth/quantity of the set
print(len(fruits))
print(len(ids))


# duplicates are removed
all_ids= {100,101,204,101}
print("All ids ",all_ids)

my_fruits = {'apple','mango','orange','grapes'}
other_fruits = {'apple','mango','orange','grapes'}
print(my_fruits==other_fruits)

# canot use index[]  , unordered 
# print(my_fruits[0])    # Error

# cannot add multiple objects list,dict,set to sets
# list_set = {[1,2] , [3,5]}   #Error

# Can't delet items with del
# del all_ids[0]

# 68. Practice - Working with Sets

# instance or not check
my_set = {1,8,345,68,943,212}
print(my_set)
print(type(my_set))
print(isinstance(my_set, set))      # True
print(len(my_set))


# Don't get get methods for sets
# can't use dict list in set
# my_set2 = {10 ,44,True,{1,5}}   # Error
# my_set2 = {10 ,44,True,[1,5]}   # Error

# for empty set use "set()"
empty_set =set()
print(type(empty_set))



'''
69. Understanding Set Theory
'''
'''
1.add() Adds a specific element to the set.
2. union() Combines two or more sets and returns a new set containing all unique elements.
3. remove() Removes a specific element from a set. Raises KeyError if the element is not found.
4. difference() Returns a new set with elements in the first set but not in the second.
5. intersection() Returns a new set with elements common to all sets.
6. discard() Removes a specific element if present, but does not raise an error if it’s missing.
7. clear() Removes all elements from the set.
8. copy() Returns a shallow copy of the set.
9. update() Adds elements from another set to the current set.
10. issubset() Checks if all elements of one set are in another.
11. issuperset() Checks if one set contains all elements of another.
12. pop() Removes and returns a random element from the set.
'''


# 1.add() 
set1 = {1, 2, 3}
set1.add(4) 
set1.add(2)
print("After Adding 4,2 to set 1 :",set1)

# 2. union() 
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print("union of set1 and set2 :",result)

# 2. remove()
set1 = {1, 2, 3}
set1.remove(2) 
print("after remove 3 from set 2 :",result)

# 3. difference() Returns a new set with elements in the first set but not in the second.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.difference(set2) 
print("difference of set1 and set2 :",result)

# 4. intersection() 
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.intersection(set2) 
print("Insertsection of set1 and set2 :",result)

# 5. discard()
set1 = {1, 2, 3}
set1.discard(2) 
set1.discard(4)
print("Discard 4 from set1",result)


# 6. clear()
set1 = {1, 2, 3}
set1.clear()
print("After Clearing set1 :",result)

# 7. copy() 
set1 = {1, 2, 3}
set2 = set1.copy()  
print("After coping set1 ,  set2 will be  :",result)

# 8. update() Adds elements from another set to the current set.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2) 
print("Upadte method",result)

# 9. issubset()
set1 = {1, 2}
set2 = {1, 2, 3}
result = set1.issubset(set2) 
print("Set1 is subset of set2 :",result)

# 10. issuperset() 
set1 = {1, 2, 3}
set2 = {1, 2}
result = set1.issuperset(set2) 
print("Set1 is superset :",result)

# 11. pop() 
set1 = {1, 2, 3}
element = set1.pop()
print("After pop mehtod the set :",result)






