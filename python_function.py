print("First try doing functions in Python\n")

def msg_func(option):
    print("Hi!")
    print("This is a function")
    print("You choose the number", option)

option = int(input())

if option == 1:
    msg_func(option)
elif option == 2:
    msg_func(option)
elif option == 3:
    msg_func(option)
else:
    print("Invalid option")