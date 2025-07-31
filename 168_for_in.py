# 168. For-In Loop

'''
for variable in iterable:
    # Code block to execute / print /action
'''

# exmaple with str
name = "Ujjwal"
for char in name:
    print(char,end=' ')
print()


# sample dict
info = {'name': 'Ujjwal', 'age': 21}

# Iterate over keys
for key in info:
    print(key, "-->", info[key])

# iterate over key-value pairs
for key, val in info.items():
    print(f"{key} -- > {val}")

# printing tuples 
for item in info.items():
    print(item)


# for ranges
for num in range(4):
    print(num)
print()
# also do start step end 
for num in range(1,10,2):
    print(num)