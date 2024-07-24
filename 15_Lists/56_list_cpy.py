# 56. Practice - Copying Lists

my_list = [10,3.14,'Hello',False]
cpy_lst = my_list
cpy_lst.append(None)
print(my_list)
print(cpy_lst)
# Check same address 
print(id(my_list)==id(cpy_lst))
# same!
print(id(my_list))
print(id(cpy_lst))

# we can create new object of the list as below using .copy()

# my_list = [10,3.14,'Hello',False]
# cpy_lst = my_list.copy()
# cpy_lst.append(None)
# print(my_list)
# print(cpy_lst)
# # Check same address 
# print(id(my_list)==id(cpy_lst))
# # same!
# print(id(my_list))
# print(id(cpy_lst))


# We can also copy the list using "list(list_name)"
list1 = [1,3.14,True,None,'Hi']
copy_list = list(list1)
print(copy_list)

# Using List slicing 
list2 = [1,1000,False,"Hello"]
copy_list1= list2[:]
print(copy_list1)


# 57. TASK - Working with Lists

# Lists : Task 1 
print("\n....Task : 1...\n")
# 1.Create a list with 5 elements of different type
first_list = [100,True,"Python",None,3.14]
print("New list is : ",first_list)

# 2. Delete thhe third element of the list 
first_list.remove("Python")
print("After removing 3rd element :",first_list)

# 3. Print the length of the list 
print("Length of List is: ",len(first_list))

# 4.Change the order of items in the list [Reverse] 
first_list.reverse()
print("Reverse List is : ",first_list)

# 5.Create an another list with two elemets 
second_list = ["Hii",False]

# 6.Expand the first list with elemets of second list
first_list.extend(second_list)
print(first_list)



# Lists : Task 2 
print("\n....Task : 2...\n")
# 1.Create two lists 
# 2.Combine two list using + oprerator
# 3.Detemine which magic method of lists is called when using the + operator
# 4.Merge lists using the magic mehtod
# 5.Print the results to the terminal
