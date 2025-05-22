# 118. Falsy and Truthy Values

'''
bool fun returns false -> Falsy
bool fun returns ture ->Truthy 
'''
# Empty /seqstr/set/list all are falsy 
# Examples
empty_dict = {}
empty_list =[]
empty_tuple=()
empty_set=set()
emt_str =""
print(bool(empty_dict))
print(bool(empty_set))
print(bool(empty_set))
print(bool(0.0))
print(bool(0))
print(bool(0j))
print(bool(None))
print(bool(False))
print(range(0))
print(bool(set()))


# more ex
my_list = [1,2,3,4]
if len(my_list) > 0:
    print("list has elements ")
    
# no need to specify any condition simply do as below
another_list=[1,3,5,7]
if another_list:    # convert boolean
    print("list has elements")
    
    
# truthy values have some value that is not empty 
info = {
    'name':'ujjwal',
    'age':21
}
print(bool(info))
print(bool(10))
print(bool([1,2,3]))
print(bool({10,20,30}))
print(bool(range(1)))
