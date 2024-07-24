# 54. Practice - Working with Lists

nums = [10,56,78,35]
print(nums)
print(type(nums))
print(isinstance(nums,list))
print(id(list))

# add new elements to nums
nums.append(100)
print(nums)
print(id(nums))   # address should not be same

# remove element 
remove_ele = nums.pop()
print(nums)
print("Removed Elelement is :",remove_ele)

# extend method
nums.extend('Ujjwal')
print(nums)

# get index 
print("Index of 10 is ",nums.index(10))

# Clear the whole list using clear()
# nums.clear()
# print(nums)

# merge two lists 
l1 = [1,3,5,7,9]
l2 = [2,4,6,8,10]
mergred_list = l1 + l2
print("Merged list : ",mergred_list)
mergred_list.sort()
print("sorted merged list :",mergred_list)

# replace elements 
my_list = [True, None, 'ABC', 10, 3.14]
my_list[2] = 'Ujjwal'
print(my_list)


#55. Copying Lists
my_cars = ['BMW','Audi','Ferrari','GWagon']
# copied_car = my_car    # copy by reference
copied_cars = my_cars[:]    # copy by reference
copied_cars.append("Jaguar")
print(copied_cars)
print(my_cars)
print(id(my_cars) == id(copied_cars))


# using copy() Methods
my_cars1 = ['Ferrari','Ambassador','GWagon','Fortuner']
copied_cars1 = my_cars1.copy()    # copy by reference
copied_cars.append("Jaguar")
print(copied_cars1)
print(my_cars1)
print(id(my_cars1) == id(copied_cars1))

# 56. Practice - Copying Lists
my_lst = [100,True,'abe',3.14]
copy_lst = my_list
copy_lst.append(None)
print(my_lst)

