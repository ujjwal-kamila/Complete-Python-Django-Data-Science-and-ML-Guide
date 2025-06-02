# 130. Practice - Filtering a List using Lambda Functions

# odd even nums in list
nums = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, nums))
odd = list(filter(lambda x: x % 2 != 0, nums))
print("Odd numbers:", odd)  
print("Even numbers:", even) 


# filter name starting with char
names = ['Amit', 'Rohan', 'Ankit', 'Sohom']
ch = input("Enter starting character: ")

starts_with_ch = list(filter(lambda name: name.startswith(ch), names))
print("Names starting with", ch, ":", starts_with_ch)


# grade for marks
marks = [95, 82, 37, 66]
grades = list(map(lambda m: 'A' 
                if m >= 90 
                else 'B' 
                if m >= 60 
                else 'F', marks))
print(grades)
