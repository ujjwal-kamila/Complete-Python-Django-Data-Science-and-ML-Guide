# 108. Callback Functions

def other_fun():
    pass

def fn_with_callback(callback_fn):
    callback_fn()
    
fn_with_callback(other_fun)