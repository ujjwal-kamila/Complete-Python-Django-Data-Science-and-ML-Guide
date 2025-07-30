# 146. Practice - Unpacking a List into Positional Arguments

def calculate_rectangle_area(length: int, width: int):
    return length * width

dimensions = [100, 20]

area = calculate_rectangle_area(*dimensions)
print(area)


# more examples using dict 
def greet(name, age):
    print(f"Hello, {name}. You are {age} years old.")

info = {"name": "Ujjwal", "age": 21}
greet(**info)
