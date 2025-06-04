# 140. TASK - Proper Error Handling


'''
# 1.Create an image_info function with one dict type parameter
# 2.Function waits for a dict that must contain at least two keys - 'image_id' and 'image_title'
# 3.Function must return a string like:
"image 'my_cat' has is 5125"
# 4. If at least one of these keys not in dict fun must generate a TypeError
# 5.Call the function and correctly handle error if it appears

'''

def image_info(image_details)->str:
    if not isinstance(image_details,dict):
        raise TypeError("Input must be a dictionary!")
    
    if 'image_id' not in image_details or 'image_title' not in image_details:
        raise TypeError("Dictionary must contain 'image id' and 'image_title")
    
    return f"Image {image_details['image_title']} has ID {image_details['image_id']}"


try:
    image = {
        'image_id' : 5125 ,
        'image_title': "my_cat",
    }
    print(image_info(image))
    img= {
        "image_title": "Makaut"
    }
    print(image_info(img))
except TypeError as e:
    print(e)
finally:
    print("\n Thank You! -- Task 1 completed...")
    
