# 187. Example - Converting Dictionary to Another Dictionary

# Swap Keys and Values
original = {'x': 1, 'y': 2, 'z': 3}

swapped = {v: k for k, v in original.items()}

print(swapped)


# have some stock price 
stocks = {
    'TCS': 92,
    'INFY': 150,
    'RELIANCE': 700,
    'HDFC': 450,
    'WIPRO': 50
}
# updated_stocks = {}
# for name, price in stocks.items():
#     updated_stocks[name] = price * 1.03
updated_stocks = {name: price * 1.03 for name, price in stocks.items()}


print(updated_stocks)
