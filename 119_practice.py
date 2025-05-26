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
