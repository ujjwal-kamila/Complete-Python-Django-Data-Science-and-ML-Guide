# 189. Example - Chaining For-In Expressions

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [num for sublist in nested_list for num in sublist]
print(flattened_list)

# more examples
result = []
for x in [1, 2, 3]:
    for y in [10, 20]:
        result.append(x * y)
print(result)