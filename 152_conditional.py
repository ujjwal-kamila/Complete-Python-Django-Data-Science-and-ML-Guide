# 152. Conditional Statements

# if Statement
age = 21

if age > 18:
    print("Can Vote!")


# if-else Statement
age = 17

if age >= 18:
    print("Can vote.")
else:
    print("Underage.")

# if-elif-else Statement
score = 79

if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: D")


# using not in conditon
logged_in = False

if not logged_in:
    print("Please log in first!")


# Ternary Operator (Inline if-else)
age = 20

status = "Adult" if age >= 18 else "Minor"
print(status)


# more examples
x = 15

if x % 2 == 0:
    print("Even")
elif not x % 5 == 0:
    print("Not divisible by 5")
else:
    print("Odd and divisible by 5")

result = "Positive" if x > 0 else "Non-positive"
print(result)


