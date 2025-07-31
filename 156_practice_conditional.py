# 156. Practice - Combining if, elif, and else Statements

# leap year chekcer
year = int(input("Enter year like (2000): "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a Leap Year")
        else:
            print(year, "is NOT a Leap Year")
    else:
        print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")


'''
simple also
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")'''
    


# shipping fee checking
def check_shipping_fee(weight):
    if weight <= 0:
        print("Invalid weight. Weight must be greater than zero")
    elif weight <= 5:
        print("The shipping fee is 5$")
    elif weight <= 15:
        print("The shipping fee is 10$")
    else:
        print("The shipping fee is 20$")

check_shipping_fee(8)