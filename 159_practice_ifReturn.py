# 159. Practice - Using if and return Statements within Functions

def calculate_price(price:float,is_member:bool):
    if is_member:
        return price - price * 0.1
    else:
        return price - price * 0.05
    
    
    
    # if is_member:
    #     discount = price * 0.1 
    # else:
    #     discount = price * 0.05
    # return price-discount

pay_res = calculate_price(1000,False)
print(pay_res)

# using keywork args : best way to do 
pay_result = calculate_price(price=1000, is_member=True)

print(pay_result)
