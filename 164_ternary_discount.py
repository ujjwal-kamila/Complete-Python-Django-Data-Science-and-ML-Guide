# 164. Example - Calculating Discounts with the Ternary Operator

def check_discount_eligibility(is_member,price):
    discount = 0.1 if is_member else 0.05
    discounted_price = price - (price * discount)
    return discounted_price

customer_memebership = True
price = float(input("Enter the price of the item: "))

final_price = check_discount_eligibility(customer_memebership,price)
print(final_price)
print(f"Discounted Price: ₹{final_price:.2f}")


