# 171. Practice - Iterating through Ranges, Strings, and Sets with For-In Loops

# char wise 
name = 'Ujjwal'
for char in name:
    print(char)
 
# iterate over set
colors = {"red", "green", "blue"}
for color in colors:
    print("My favourite color is :",color)


# count vowels in a str 
text = "hello world"
count = 0
for ch in text:
    if ch in "aeiou":
        count += 1
print("Vowels:", count)
