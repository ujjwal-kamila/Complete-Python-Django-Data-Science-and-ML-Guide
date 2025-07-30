# 149. Dictionary Unpacking Operator **

info = {
    'name':'Ujjwal',
    'age':21
}

# unpacking dict and add key values & can update values also after unpack
updatd_info = {
    **info,
    #can updte values 
    'email': 'ujjwal@gmail.com'
}

print(info)
print(updatd_info)

# merging two dict using **
# as examlpe :
dict1 = {
    'username': 'ujjwal_kamila',
    'email': 'ujjwal@gmail.com'
}
dict2 = {
    'password': 'Pass@123',
    'role': 'admin'
}

# merging using **
merged_dict = {
    **dict1,
    **dict2
}

print("\nMerged dict ",merged_dict)


# merging dict using or'|' operator
new_dict = dict1 | dict2
print("merged dict :",new_dict)
