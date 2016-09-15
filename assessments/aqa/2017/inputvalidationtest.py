while True:
    
    choice = ""

    while choice not in ["y", "n", "quit", "q"]:
        choice = input("enter y, n, quit or q to proceed: ").lower()
        if choice not in ["y", "n", "quit", "q"]:
            print("Invalid input, try again.")

    print(choice)

    if choice in ["q", "quit"]:
        break

print("finished")
