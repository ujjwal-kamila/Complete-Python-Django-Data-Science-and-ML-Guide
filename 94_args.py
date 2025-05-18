# 94. Practice - Using *args to Gather Positional Arguments into a Tuple

def sort_nums(*args):
    # print(args)
    for arg in args:
        print(arg)
    return sorted(args)
        
sorted_nums = sort_nums(3,6,1,89)
print("sorted nums :",sorted_nums)


sorted_nums = sort_nums(100,8,9,5,2,1)
print("sorted nums :",sorted_nums)


# 95. Keyword Arguments
# sample ex
def get_info(name,address):
    info = f"{name} residing in {address}"
    return info 

# for more readable use keyword args
print_info = get_info(name = 'Ujjwal',address='Kalyani')
print(print_info)

# merge args to a dict
def get_person_info(**person):
    print(person)
    print(type(person))
    
    info = (
        f"{person['name']} located at "
        f"{person['address']}"
    )
    return info
    
info = get_person_info(name = 'Ujjwal',address='Kalyani')
print(info)

print("\n\n")

# 96. Practice - Working with Keyword Arguments
def post_info(name,commit_qty,day):
    res = f'{name} commits {commit_qty} Codes on {day}'
    return res

# way to do fun call as below ex
info = post_info('Ujjwal',5,'Monday')
print(info)

# wrong way 
info = post_info('Monday','Ujjwal',5)hoin
print(info)        # wrong output

# To tackle this we have to use keyword args as ex
info1 = post_info(name='Ujjwal',commit_qty=5,day='Monday')
info2 = post_info(commit_qty=10,day='Sunday',name='Ujjwal')    # for keyword args order doesn't matter 
print(info1)
print(info2)

