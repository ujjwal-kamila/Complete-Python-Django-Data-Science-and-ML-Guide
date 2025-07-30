# 150. Practice - Using the Dictionary Unpacking Operator

person = {
    'name':'ujjwal',
    'age':21
}

# create a copy of the dict and upadte values
# using noramly 
# other_person = person.copy()
# other_person['age']= 25

# using unpacking method
other_person = {
    **person,
    'age':25
}

print(person)
print(other_person)