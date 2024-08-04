# 52. Lists :  ordered seqence of elements 

l = [1,3,5,7]  #list declearation
print(l)

# Examples 
# Two lists with same elemnet in another index
my_fruits = ['apple','banana','pineapple','mango']
other_fruits = ['banana','pineapple','apple','mango']
# these two lists are not equal 
print(my_fruits ==  other_fruits)

# empty list
lst = []
# to get length of the list use len()
print(len(lst))
print("length of my_fruits is ",len(my_fruits))

id = [102,401,493,804,158]
print("Lengh of ids is ",len(id))

# Acccessing single element of the list
print(id[0])
print(id[1])
print(id[4])
# get last element 
print(my_fruits[-1])

# more exmaples 
marks = [5,7,"Ujjwal",True,8,9,10,12,15]
print(marks)
print(type(marks)) 
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])

if 7 in marks:
    print("Yes")
else:
    print("No")

#same things applies for strings as well 
if "ujw" in "Ujjwal":
    print("Yes")
else:
    print("No")

# more exaples of accessing elemets 
print(marks) #prints all elem in marks 
print(marks[:])  #prints all elem in marks 
print(marks[1:-1])
print(marks[1:8])
print(marks[1:8:2])  #jump index is 2 so jump 2
# print(marks[1000])  # index error

# print list of 1 to 10 using loop
lst = [i for i  in range(10)]
print(lst) 

# print list of square of 1 to 10 using loop
lst = [i*i for i  in range(10)]
print(lst) 

# print list of even numbers between 1 to 10 using loop
lst = [i*i for i  in range(10) if i%2==0] # divisable by 2 Even numbers 
print(lst) 


# list elememt deletion 
input_lst = [ 'True' , 'Hii', '@@' , 10.77]
print(len(input_lst))

# delete an element  
del input_lst [1]
print(input_lst)
print(len(input_lst))

del input_lst[-1]
print(input_lst)
print(len(input_lst))


# List of Dictionaries
users = [ 
    {
    'usr_id' : 1490,
    'usr_name':'Ujjwal',
    },    
    {
    'usr_id' : 1788,
    'usr_name':'Rudra',
    },
    {
    'usr_id' : 1920,
    'usr_name':'Shubham',
    },
]
print("length of user is :",len(users))
print(users[1] ['usr_id'])
print(users[0] ['usr_name'])


# Create list from strings
# Let's make some strings
str1 = 'mango'
str2 = 'apple'
str3 = 'cherry'
str4 = 'grapes'
# let's make a list of them
all_fruits = [str1, str2, str3, str4]
print("All fruits are : ",all_fruits)
print(type(all_fruits))