# 113. Practice - Using the Global Keyword

count = 0
def inc_counter(value = 1):
    """Increment counter by value

    Args:
        value (int, optional): _description_. Defaults to 1.
    """
    global count
    count  += value
    
    
def dec_counter(value =1):
    """Decrement counter by Value

    Args:
        value (int, optional): _description_. Defaults to 1.
    """
    global count
    count -=value

inc_counter(5)
print(count)    # 5
inc_counter(10)
print(count)    # 15
dec_counter(10)
print(count)    # 5