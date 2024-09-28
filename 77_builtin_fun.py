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

# enumerate mehtod
my_list = ['apple', 'banana', 'cherry']
result = enumerate(my_list)
print(list(result))