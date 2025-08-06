# 182. Practice - Using Dictionary Comprehension

# examples
fruits = ["apple", "banana", "cherry","grapes"]

fruit_len = { fruit:len(fruit) for fruit in fruits}

print(fruit_len)


# Characters and their ASCII values:
ascii_dict = {char: ord(char) for char in 'abcde'}
print(ascii_dict)
