# 124. Practice - Examples with Logical Operators

my_list = []
other_list = [1,2,'a']

# check empty or not
if other_list:
    print("not empty")
else:
    print("Empty")
    
    
print(my_list or other_list)
print(not not (my_list or other_list))


# Vowel check using or operator
ch = input("Enter a character like 'a' : ")
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or \
   ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
    print("Vowel")        # \ for read ability
else:
    print("Not a vowel")
    
    
# simple method not using or 
ch = input("Enter a character like 'a' : ")
if ch in 'aeiouAEIOU':
    print("Vowel")
else:
    print("Not a vowel")
