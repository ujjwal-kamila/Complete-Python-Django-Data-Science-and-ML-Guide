# 43. Practice - Integers Manipulation

# We can do all arithemetci operations such as below:
my_num = 10_000
other_num = 5_000
sum = my_num + other_num
sub = my_num - other_num
print("Sum is : ",sum)
print("Subtraction is : ",sub)

# converting str to int 
# Taking user input 
input_str = input("Enter any numbers : ")
print(type(input_str))    # <class 'str'>

# converting into str
# Add execption handeling
try:
    input = int(input_str)
    print(type(input))    #<class 'int'>
except ValueError:
    print("Unable to convert to intger")
    

