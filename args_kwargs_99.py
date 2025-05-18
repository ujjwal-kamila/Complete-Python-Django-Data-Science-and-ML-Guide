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

# positional arguments 
def send_email(to,sub,*args):
    print(f"Send email to : {to}")
    print(f"Email subject is : {sub}")
    #or can do loop 
    if args:
        print("\nAdditonal argmunets : ",end = ' ')
        for i in args:
            print(i,end ='  ')
    # or can simply return args and print it 
    return args



# call as positional args
all_args = send_email("abc@gmail.com","Hello World!" ,"xyz@gmail.com","Hello There !")
print("\nextra args :  ",all_args)

