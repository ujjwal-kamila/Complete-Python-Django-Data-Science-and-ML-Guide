# 170. Practice - Iterating through Dictionaries using For-In Loops


product_prices = {
    'PC': 100000,
    'Mobile Phone': 20000,
    'Tablet': 35000,
    'Camera': 70000
}

for item in product_prices.items():
    # tuple unpack
    key,value = item
    print(key,value)
print()
# using key valyes
for key,value in product_prices.items():
    print(key,value)
    
# store the result in another list
expensive_items = []
for key, value in product_prices.items():
    if value > 50000:
        expensive_items.append((key, value))

print("Expensive items:", expensive_items)


# Print Student marks and calculate Average
student_marks = {
    'Aashiq': 85,
    'Ujjwal': 90,
    'Raj': 78,
    'Rajat': 92
}

# Task:
# 1. Print each student's name and their marks
# 2. Calculate the average marks and print it
total = 0 
count = 0
for name ,makrs in student_marks.items():
    print(f"{name} got {makrs}")
    total +=makrs
    count +=1

avg=total/count
print(f"\nAverage marks : {avg}")




