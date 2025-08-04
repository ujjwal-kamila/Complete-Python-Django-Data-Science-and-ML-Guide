# 175. Example - Making Selections with the While Loop

# selection using while loop 

selected_option = 0

while selected_option not in range(1,5):
    print("Menu")
    print("1. Start the Game! ")
    print("2. Load the Server ")
    print("3. Quit ")
    try:
        selected_option = int(input("Enter the choice (1-4) : "))
    except ValueError as e:
        print(e)
        print("Try to select the option again")
if selected_option == 1:
    print("1. Start the Game! ")
if selected_option == 2:
    print("2.Loading the Game")
if selected_option == 3:
    print("Quit...")



