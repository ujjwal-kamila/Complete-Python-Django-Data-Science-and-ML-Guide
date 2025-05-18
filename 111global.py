# 111. The Global Keyword

# creating global variable in the fun

def my_fun():
    global a
    a = 100
my_fun()
print(a)

# using global var in fun
pi = 3
# print(pi)
def cal_area(r):
    global pi 
    pi= 3.14
    area = pi * r * r
    print("Area of circle : ",area)

cal_area(4)
print(pi)


# 112. Practice - Global and Local Variables


c = False
def mult(a,b):
    c = a * b
    return c
print(mult(20,5))
print(c)
    
