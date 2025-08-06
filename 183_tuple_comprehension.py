# 183. Practice - Utilizing Tuple Comprehension


t = tuple(x for x in range(5))
print(t)

names = ['Ujjwal','Aashiq','raj']

name_lenths = tuple(len(name) for name in names)
print(name_lenths)

# tuple of even nums 
even_numbers = tuple(x for x in range(1, 20) if x % 2 == 0)
print(even_numbers)
