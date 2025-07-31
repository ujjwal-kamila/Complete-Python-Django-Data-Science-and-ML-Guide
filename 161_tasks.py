# 161. TASK - Conditional Statements

# 1.Create an route_info function which accepts dictionary as parameter
# 2.If the dict has a distance key and its value is an integer 
# return the string "Distance to your destination is <Distance >"

# 3.Other wise if there are speed and time keys in the dict return thr string 
#  "Distance to your destination is <speed * time >"



# 1 
def route_info(data):
    if 'distance' in data and  isinstance(data['distance'],int):
        return  f"Distance to your destination is : {data['distance']}"
    elif 'speed' in data and 'time'in data:
        return  f"Distance to your destination is : {data['speed'] * data['time']}"
    
    else:
        return "Wrong data "
    
# test cases
d1 = {
    'distance': 120
}

d2 = {
    'speed': 60,
    'time': 2
}


res1= route_info(d1)
print(res1)
res2 = route_info(d2)
print(res2)
