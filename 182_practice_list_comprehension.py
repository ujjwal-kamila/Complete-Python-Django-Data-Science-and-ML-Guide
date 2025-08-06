# 181. Practice - Using List Comprehension

# list to list
nums = [1,3.14,15,100]

# new list as square of all elemments
square_nums = []
for num in nums:
    square_nums.append(num*num)
print("using loop",square_nums)

# using list comprehension
sq_nums = [num*num for num in nums ]
print("using list comprehension",sq_nums)