# 193. Example - Verifying User Permissions with Decorator Functions

# auth check function
def is_user_authenticated():
    return True

# Decorator to check user authentication
def check_user_auth(fn):
    def wrappper(*args,**kwargs):
        # Check if user is authenticated
        if is_user_authenticated():
            print("User is authenticated!..")
            return fn(*args,**kwargs)
        else:
            # Raise error if not authenticated
            raise Exception("User is not authenticated ")
    return wrappper

# Apply decorator to sensitive function
@check_user_auth
def do_sensitive_job():
    # perform action if user is authenticated
    print("Some sensitive job results")

# Call the fun
do_sensitive_job()