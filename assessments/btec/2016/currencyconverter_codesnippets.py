# version 1: does not require try/except
# get user input and check if valid
while menu != "0" and menu != "1" and menu !="2" and menu != "3":
    menu = input("Enter option (0-3): ")

# version 2: uses try/except, makes conditionals easier to read
# get user input and check if valid
while menu < 0 or menu > 3:
    try:
        menu = int(input("Enter option (0-3): "))
        if menu < 0 or menu > 3:
            print("Invalid option!")
    except:
        print("Invalid option!")
