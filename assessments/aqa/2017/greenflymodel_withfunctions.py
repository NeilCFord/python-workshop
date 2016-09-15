
def display_main_menu():
    menu = 99
    # display main menu
    print("Select option:")
    print("0: Set the Generation 0 values")
    print("1: Display Generation 0 values")
    print("2: Run the model")
    print("3: Export the data")
    print("4: Quit the program")

    menu =input("Enter option (0-4): ")

    return menu

# main program loop
while True:

    choice = display_main_menu()

    if choice == "0":
        # set generation 0 values
        print(choice)
        break

    elif choice == "1":
        # display generation 0 values
        print(choice)
        break

    elif choice == "2":
        # display generation 0 values
        print(choice)
        break

    elif choice == "3":
        # display generation 0 values
        print(choice)
        break

    elif choice == "4":
        # display generation 0 values
        print(choice)
        break
        
    else:
        print("Invalid input!")
        print("")
        
