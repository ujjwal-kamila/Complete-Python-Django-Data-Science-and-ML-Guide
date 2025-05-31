


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
