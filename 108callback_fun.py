# 108. Callback Functions : called inside of another fun 

def other_fun():
    print("I am CallBack Function ")

def fn_with_callback(callback_fn):
    callback_fn()
# calling a fun with its name in anohter fun param
fn_with_callback(other_fun)


# more examples 
def greet(name):
    print("Hello", name)

def say_hello(callback):
    callback("Ujjwal Kamia")  # calls greet("Ujjwal")

say_hello(greet)


# Function to check if a number is odd or even
def odd_even(num):
    if(num % 2 == 0):
        print("Entered Number is Even ")
    else:
        print("Entered number is Odd ")

# calls the callback function using the number
def process_num(num, callback_fn):
    callback_fn(num) # calling: odd_even(num)

entered_num = int(input("Enter any integer : "))

process_num(entered_num, odd_even)



# send data example:
def send_data(data):
    pass


def process_data(input_data,send_data):
    updated_data = input_data.copy()
    send_data(updated_data)
    print(updated_data)

process_data({'name':'Ujjwal'},send_data)
