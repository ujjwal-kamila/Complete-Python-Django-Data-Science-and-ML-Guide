# 97. Practice - Using **kwargs to Merge Keyword Arguments in a Dictionary

def price_info(**product):
    product_title = product["product_title"]
    product_price = product["product_price"]
    print(f"{product_title} costs {product_price}₹")
    print(product)
    
info = price_info(product_title="Bottle of water", product_price=1)



'''
✅Tasks : 01✅
'''

'''
1. Rewrite the call to the merger_lists_to_dict function from previous task so that is uses keyword arguments 
2. Add another function call . First argument in this should be positional argumment and the second one is ketword argument 


'''
# prev taks function as below
def merge_lists_to_dict(list1,list2):
    zip_res= zip(list1,list2)
    result = dict(zip_res)
    return result
# Create two lists as Key Value 
l1 = ["name",'branch','roll',"age","can_vote"]
l2 = ["Ujjwal","CSE",22033,20,True]
# Call using keyword arguments
res = merge_lists_to_dict(l1,l2)
print("Combine Dict is :",res)
print("\nTask 1 ans : ✅✅ \n\n")



# 1. call merge lists to dict function 
result = merge_lists_to_dict(list1=l1,list2=l2)

# 2. Add another function call: 1st = positional, 2nd = keyword
res2= merge_lists_to_dict(l1, list2 = ["Aashiq","IT",12345,22,True])
print("Second combined dict is :", res2)


'''
✅Tasks : 2✅
'''
print("\nTASK  02 ans ✅ \n")

# 1.create an update car info function in which all named argumnets will be combined into a car dictionary
# 2. add a new_avilable key to the dictionary with the value true 
# 3. return modified dict from the function
# 4. call another functtion brand and price keyword args their values can be any 
# 5. output the result of the function call to the terminal

# 1.create update_car_info function 
def update_car_info(**car):
    car["new_available"] = True  # 2.add key
    return car      #3. return dict

# 4.create fun brand and price key args
def car_info(brand,price):    
    return update_car_info(brand =brand,
    price= price)

print(car_info("Audi",780000))

