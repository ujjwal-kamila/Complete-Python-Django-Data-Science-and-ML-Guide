# 102. Default Function Parameters

# option paramter assign to some value in in fun as eg
def multilpy_by(value,multiplier=1):
    return value * multiplier


# test 
res = multilpy_by(10)
print(f"10 multiply to default : ",res)
res = multilpy_by(10,5)
print(f"10 multiply to 5 : ",res)

# example : a function that creates a new post by copying an existing dictionary and automatically adds the current weekday as a new key
# 103. Practice - Using Default Function Parameters

from datetime import date
def get_weekday():
    return date.today().strftime('%A')

print(get_weekday())  # return current day 

def create_Newpost(post,weekday=get_weekday()):
    post_copy = post.copy()
    post_copy['created_on_weekday'] = weekday
    return post_copy

sample_post = {
    'id' : 101,
    'user':'Ujjwal',
}

s_post = {
    'id' : 105,
    'user':'Kamila81',
}

# pos args
res = create_Newpost(sample_post)
print(res)
# keyword args
new_res = create_Newpost(post=s_post,weekday='Sunday')
print(new_res)




