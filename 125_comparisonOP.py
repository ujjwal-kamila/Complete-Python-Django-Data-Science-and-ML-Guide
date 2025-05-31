# 125. Practice - Comparison Operators

# Comparison of all operators using magic method class
class MyNumber:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __le__(self, other):
        return self.value <= other.value

a = MyNumber(10)
b = MyNumber(20)

print(a == b) 
print(a != b) 
print(a < b)   
print(a > b)  

# use of some built-in functions

# simple ex
name = 'Ujjwal'
if len(name) > 5:
    print(f"{name} is longer that 5 char")
    
tup1 = (2,6,8,13,9)
if sum(tup1)>=30:
    print("Sum is greater than 30")
    
my_nums = [12,10,0,8,3,1]
print("Sorted Elements",sorted(my_nums))

other_nums =[1.5, 3.14,5.89,10.9]
if other_nums == sorted(other_nums):
    print("List is already sorted! ")
    
print(id(other_nums)==id(sorted(other_nums)))   # False