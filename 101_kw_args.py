# 101. Practice - Gathering All Keyword Arguments into the **kwargs Dictionary

def send_email(to,sub,*args,**kwargs):
    print(f"Send email to : {to}")
    print(f"Email subject is : {sub}")
    #or can do loop 
    if args:
        print("\nAdditonal argmunets : ",end = ' ')
        for i in args:
            print(i,end ='  ')


    # for kwargs
    if kwargs:
        print("\nKeyword args :")
        for key in list(kwargs):
            print(f"{key} : {kwargs[key]}ṣ")
    



    return args



# call as positional args
all_args = send_email("abc@gmail.com","Hello World!" ,"xyz@gmail.com","Hello There !",bcc='ujjwal@gmail.com',photo='id.png')
print("\nextra args :  ",all_args)

print("\n\n")
send_email("ujjwalkamiila2004@gmail.com","How are you !")