# 45. Practice - Floating-Point Numbers Manipulation

avg_rating = 8.84
print(type(avg_rating))

# check int or not using is_integer()
print(avg_rating.is_integer())    # False

# using round make it int
print(round(avg_rating))     # 9
print(int(avg_rating))       # 8
print(float(200))
print(int(200.0))



# 46. Working with Complex Numbers
# Complex num has two part "Real" and "Imagenary"
complex_a = 3 + 5j
complex_b = 4 + 3j

sum = complex_a + complex_b
print(sum)
print(type(sum))   # <class complex>