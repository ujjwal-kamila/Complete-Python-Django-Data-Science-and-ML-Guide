# 178. TASK - While Loop

'''
1.Create a loop in which you need to ask the user to enter two numbers in the terminal
2.Print the result of the division of the first number by the second number in the terminal
3.After that, ask the user if he wants to continue yes/no
4.If the answer is no, you need to exit the loop
5.other wise repeat the process
'''

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = num1 / num2
        print(f"Result of division {num1} / {num2}:", result)

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter valid numbers.")

    choice = input("Do you want to continue? (yes/no): ")
    if choice == "no":
        print("Exiting the loop...")
        break