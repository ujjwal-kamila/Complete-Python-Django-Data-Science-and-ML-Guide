# 186. Practice - Short For-In Loops with Conditional Statements

person = {
    'name': 'ujjwal',
    'fav_num': 7,
    'is_instructor': True
}

person_str_val = [value for value in person.values() if  type(value)==str]
print(person_str_val)