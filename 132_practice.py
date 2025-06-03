# 132. Practice - Using Different Error Classes in the Try and Except




try:
    salary = int(input("Enter salary amount : "))
    days= int(input("Enter day quantity : "))
    salary_perDay = round(salary / days)
    print("salary per day : ",salary_perDay)
except ValueError:
    print("ValueError - cannot convert value to integer!")
except ZeroDivisionError:
    print("Cannot division by zero!")
    
except Exception as e:
        print(e)
print("OK")