# 53. List Methods
'''
append(): Adds an item to the end of the list.
pop(): Removes and returns the item at a given index.
remove(): Removes the first occurrence of a value.
insert(): Inserts an item at a specified position.
sort(): Sorts the list in ascending order.
index(): Returns the index of a value.
copy(): Returns a shallow copy of the list.
clear(): Removes all items from the list.
reverse(): Reverses the list in place.
count(): Returns the number of occurrences of a value.
extend(): Adds elements of an iterable to the list.
'''

# Let's try with more examples
even_lst = []
print(even_lst)
# append even values 
even_lst.append('2')
even_lst.append('4')
even_lst.append('6')
even_lst.append('8')
even_lst.append('10')
print("After append even values :",even_lst)
print(len(even_lst))

# Pop() method
lst = [False,3110,'Hii','😁',3.14]
print(lst)
lst.pop()    # remove last element 3.14
print(lst)

lst.pop(0)   # remove 0th element False
print(lst)

removed_element = lst.pop()   # remove 0th element 3110
print(lst)
print("Removed Element is",removed_element)


# sort() method
list1 = [5,2,0,10,4,7,6,3,1,9]
list1.sort()
print(list1)

# put in reverse way as Descending order
list1.sort(reverse=True)   # named args or keyboard args 
print(list1)


# conversion to a list 
# from str to list
greeting = 'Hello , How are You'
greeting_lst = list(greeting)
print(greeting_lst)

# from dict to list 
dict = {
    'a' : 100 ,
    'b': True ,
    'c': 3.14 ,
    'd': 'Ujjwal'
}
# we get only keys as a,b,c,d
dict_lst = list(dict)
print(dict_lst)

# Arithemetic operations in list
ratings = [1.5 , 5.6 ,9.8,6.8]
print(min(ratings))
print(max(ratings))
print(sum(ratings))
print(sum(ratings) / len(ratings))

# Combine or concate two lists 
my_list1 = [3.41,8.5,1.8]
my_list2 = [6.7,5.9,9.6]
all_list = my_list1 + my_list2
print(f"Sum of list1 and list2 is",all_list)


# list slicing "list[start:end::Stepvalue]"
odd_num= [ 1,3,5,7,9,11,13,17]
first_two_num = odd_num[:2]
print("First two numbers is :",first_two_num)

middle_num = odd_num[2:-2]
print("middle numbers is :",middle_num)

last_two_num = odd_num[-2:]
print("Last two numbers is :",last_two_num)

