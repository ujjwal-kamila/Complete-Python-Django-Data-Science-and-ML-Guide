# 77. Built-in Functions for Sequences

'''
len(): Counts elements in iterable.
sum(): Adds elements in iterable.
min(): Finds smallest in iterable.
filter(): Selects elements meeting condition.
max(): Finds largest in iterable.
sorted(): Orders elements in iterable.
reversed(): Reverses elements in iterable.
zip(): Pairs elements from iterables.
enumerate(): Indexes elements in iterable.
'''

# examples
list1 = [20,10,45,25]
print("Lenth of the list :",len(list1))
print("Sum of the list :",sum(list1))
print("Smallest element of the list :",min(list1))
print("Largest of the list :",max(list1))
print("Largest of the list :",max(list1))
result =filter(lambda x:x%2 == 0,list1)
print("Filter divsion by 2 ",list(result))
print("Sorted list is",sorted(list1))
print("Reversed list is :",list(reversed(list1)))

# zip method
l1 = [1,2,3,4,5,6]
l2 = ['a','b','c','d']
res = zip(l1,l2)
print("Zip of l1 and l2 :",list(res))

# covert zip to dict 
result = zip(l1,l2)
dict_zip_objects = dict(result)

print("Dict of result : ",dict_zip_objects)

# enumerate mehtod
my_list = ['apple', 'banana', 'cherry']
result = enumerate(my_list)
print(list(result))


# 79. Practice - Working with zip Objects
products = ['tablet','laptop','desktop','phone']
qunatities = [101,201,301,401,1000]
tag = 'ABCD'

products_qunatities = zip(products,qunatities,tag)
print(type(products_qunatities))
print(products_qunatities)

# iteration over zip object 
'''
for product in products_qunatities:
    print(product)
    print(product[0])
'''
# print using list 
all_list = list(products_qunatities)
print(all_list)


'''
80. Practice - Converting a zip Object to a Dictionary
'''
# for convert zip to dict need two elemenets z1,z2
z1 = ['laptop','tablet','smartphone']
z2  = [6,6,10]
zip_z1z2 = zip (z1,z2)
zip_z1z2_dict = dict(zip_z1z2)
print("After conversion to dict :",zip_z1z2_dict)


'''
81. Comparison of Different Sequences
'''
#        mutable ordered identical 
'''
    list     ✅    ✅    ✅
    tuple/str❌    ✅    ✅ 
    set/dict ✅    ❌    ❌
    range    ❌    ✅    ❌
'''