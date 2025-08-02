# 172. TASKS - Working with For-In Loops

# Task 1
'''
1. Create a dict_to_list function that will convert the dict to a list of tuples
2. Function should accept the dict, and return a list of tuples, each tuple must have pairs (key, value) from the dict
3. If the value of the key is an integer, it must be multiplied by 2 before adding it to the tuple
'''

# list1 = list(info.items())
# print(list1)

def dict_to_list(data):
    res = [ ]
    for key,value in data.items():
        if isinstance(value,int):
            value *= 2
        res.append((key,value))
    return res

info= {
    'name':'ujjwal',
    'age':21

}

ans = dict_to_list(info)
print(ans)



# Task 2
'''

1. Create a filter_list function that will filter the list
2. The function will accept two arguments - list and value type, for example int, str or bool
3. Function should return a new list in which only values of the specific type that was passed in the function call as the second argument will remain
4. The function can be called, for example, as follows:
filter_list([35, True, 'abc', 10], int) and function will return [35, 10]

'''

def filter_list(data, value_type):
    res = []
    for item in data:
        if isinstance(item, value_type):
            if value_type is int and isinstance(item, bool):
                continue  # Skip True,False as bool also a subclass of int 
            res.append(item)
    return res

data = [35, True,58, 'abc', 10]
print(filter_list(data, int))  


def filtered_list(data, value_type):
    return [item for item in data if isinstance(item, value_type) and not (value_type is int and isinstance(item, bool))]

data = [31, True,58, 'abc', 10]
print(filtered_list(data, int))  
