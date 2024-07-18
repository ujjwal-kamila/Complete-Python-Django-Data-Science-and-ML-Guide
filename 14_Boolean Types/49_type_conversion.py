# 49. Type Conversion

# Type conversion is nessesary for operations & handle correct data types 
# print(10 + '5')  # type error 
print( 10 + int('5'))

# more examples 
int_num = 5
float_num = 3.14
print(f"sum of {int_num} and {float_num} is :",int_num+float_num)

# how the addition performed "magic method"
print(int_num.__add__(float_num))    # NoImplemented 
print(float_num.__radd__(int_num))   # 8.14


# True indicate one value
bool_val = True
int_val = 10
print(f"Sum of {bool_val} and {int_val} is :",bool_val+int_val)