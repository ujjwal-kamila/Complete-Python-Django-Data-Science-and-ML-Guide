# 209. Inheritance from Other Classes

# sample example 
# class that extends Python's built-in list
class ExtendedLlist(list):
    def print_list_info(self):
        # len(self) calls list.__len__()
        print(f"List has {len(self)} elements")

# create an object
custom_list = ExtendedLlist([1,2,3,4,5])
# Call your method
custom_list.print_list_info()


