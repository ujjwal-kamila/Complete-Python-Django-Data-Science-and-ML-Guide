# 89. Mutable and Immutable Arguments in Function Calls

# Ex: Immutable objcet as a,b as args
def main_fun(a,b):
    a = a+5 
    c = a+b
    return c

num1 = 10
num2 = 5
result = main_fun(num1,num2)
print("Result is ",result)
print("Value of num 1 is : ",num1)    # not change Actual value

# Ex: Mutable object as dict args
def incre_age(person):
    person['age'] += 5
    return person

person1 = {
    'name':'Ujjwal',
    'age':20
}

print("age before run the fun : ",person1['age'])
incre_age(person1)
# Actual value changed 
print("age after run the fun:", person1['age'])


# avoid this same object using .copy() methods

# Example: Avoid changing the actual value of a mutable object
def incre_age(person):
    # Work with a copy instead of the original
    person_copy = person.copy()  # Creates a shallow copy
    person_copy['age'] += 5
    return person_copy

person1 = {
    'name': 'Ujjwal',
    'age': 20
}

updated_person = incre_age(person1)
print("Updated age:", updated_person['age'])  
print("Original age:", person1['age'])
