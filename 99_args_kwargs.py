# 99. Args and kwargs

# crate a fun with args and kwargs
def my_args(*args,**kwargs):
    print("Positional arguments : ",args)
    print("\nKeyword argumetns : ",kwargs)

# positional args merged into -> tuple() and keyword args -> dict{}
my_args (10 , 3.14, True , pi =3.14 , key = 20 , name = 'Ujjwal')

# ✅ Positional first, then keyword
# my_args ( key = 20 , name = 'Ujjwal',10 , 3.14, True , pi =3.14 ) ## error positon of positional args are first



'''

100. Practice - Gathering Positional Arguments into the *args Tuple

'''


