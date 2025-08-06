# 188. TASKS - Short For-In Loops
''' TASK : 01 '''
# 1. Create a dictionary with several keys, the values of which should be of type str
# 2. Create a new dictionary based on an existing one, in which the values of all keys must be in upper case
# 3. Print the resulting dictionary to the terminal

# 1
info = {
    'name':'Ujjwal',
    'title':'Kamila',
    'place':'Kalyani',
    'brach':'Btech.CSE'
}
print("Old dict :",info)
# 2
new_info= {key.upper():val  for key,val in info.items() }
# 3
print("Updated dictionary : ",new_info)

# 1.Create a list with elements of type str
# 2. From this list, create a new list that will contain only strings which have more than 5 characters
# 3. Reverse the order of the elements in the list
# 4. Print the resulting list to the terminal

''' TASK : 02 '''
# 1
my_list = ['Web Dev','Python','Coder','Programmer','Hacker','AI/ML']

# 2
new_list = [word for word in my_list if len(word)>5 ]  #can add here also [::-1]
print("new list : ",new_list)

# 3
new_list.reverse()    
# or use reversed_words = long_words[::-1]


# 4
print("Reversed list :",new_list)