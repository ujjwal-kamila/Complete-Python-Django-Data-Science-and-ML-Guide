# 74. Ranges : ordered immutable seq of elements 
my_range = range(10)

print(type(range))
print(list(my_range))   # prints upto 0 - 9

'''
range(start,end,stepvalue)   'all should be int '
'''

# examples
new_range = range(0,20,2)
print(list(new_range))

# also print using loop
for i in new_range:
    print(i,end ='  ')
print('\n')
    
# Accessing using index 
print(new_range[1])
# print(new_range[10])  # index Error
print(new_range[5])

# directly use range in loop
for i in range(0,5):
    print(i)        # prints 0 - 5



# 75. Practice - Range Manipulation
# odd  nums
odd_nums = range(1,100,2)
even_nums = range(0,100,2)

#using list method
print("Odd numbers 1-100 :\n ",list(odd_nums))
print('\n')
print("Even numbers 0-100 :\n ",list(even_nums))

# using loop
print("\nall odd numbers 1-100 : ")
for i in odd_nums:
    print(i,end=' ')
    
print('\n')

print("\nall Even numbers 0-100 : ")
for i in even_nums:
    print(i,end=' ')
print('\n')


# 76. Practice - Range Methods and Attributes
odd_num = range(1,20,2)
for i in odd_num:
    print(i,end = ' ',)
print('\n')
# index method
print("index of 11 :",odd_num.index(11))

# count method
print("count of 19 :",odd_num.count(19))

print(odd_num.start)
print(odd_num.stop)
print(odd_num.step)

# Conversion to tuple list set
print(list(odd_num))
print(tuple(odd_num))
print(set(odd_num))