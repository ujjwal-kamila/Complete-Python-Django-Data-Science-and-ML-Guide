# 34. Practice - Using the built-in isinstance() Function

# Check given input if instance or not 
print(isinstance(555, int))
print(isinstance('Ujjwal', str))
# print(isinstance('Hello' == int)) # Error

# Object is a root class for all objects let's example

print(isinstance('Ujjwal',object))   # True
print(isinstance(787,object))   # True

print(type(object))