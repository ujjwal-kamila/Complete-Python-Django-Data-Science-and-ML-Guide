# 119.Practice Falsy and Truthy values 

# examples:
def is_truthy(val):
    return bool(val)

print(is_truthy(0))
print(is_truthy("Python"))
print(is_truthy([]))

# example : using oops concept creating class and object
class MyObject:
    def __init__(self, data):
        self.data = data

    def __bool__(self):
        return bool(self.data)

obj1 = MyObject([])
obj2 = MyObject([1, 2])

print(bool(obj1))
print(bool(obj2))
print()
print()


# create a fun that checks the dict is empty or not and value is present or not
def check_dict(my_dict,val_to_find):
    if not my_dict:
        print("The dictionary is empty..")
    else:
        print("The dictionary is not empty..")
        if val_to_find in my_dict.values():
            print(f"The Value '{val_to_find}' is present is dictionary..")
        else:
            print(f"The Value '{val_to_find}' is NOT present is dictionary..")

info = {
    'name': 'Ujjwal',
    'age': 21    
}

check_dict(info,'Ujjwal')
check_dict(info,21)

d3 = {}
check_dict(d3, "anything")