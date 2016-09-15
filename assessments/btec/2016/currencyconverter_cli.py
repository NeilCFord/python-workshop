# BTEC Software Development Assignment 2016
# Sample Solution - NOT FOR DISTRIBUTION
# Neil Ford - neil.ford@cpdforteachers.com

# program to convert to and from British Pounds to a selection of
# foriegn currencies and to allow for the exchange rates to be
# changed and saved.

# import modules (if required)

# define functions
# display currency list and return selection
def display_currency_menu():
    for i in range(len(currencies)):
        print(str(i) + ": " + currencies[i])

    menu = 99
    while menu < 0 or menu > currency_index_max:
        try:
            menu = int(input("Enter option (0-" + str(currency_index_max) +"): "))
            if menu < 0 or menu > currency_index_max:
                print("Invalid option!")
        except:
            print("Invalid option!")

    return menu

# write exchange rate data to disk
def file_write():
    # how many records we have
    records = len(currencies)

    # open the file for write
    fh = open('currencyrates.txt', 'w')

    # loop through the records
    record = 0
    while record < records:
              
        # get the currency and rate from the lists
        currency = currencies[record]
        rate = rates[record]
              
        # write them to the file
        fh.write(currency + ',' + str(rate) + '\n')
        record = record + 1

    # close file
    fh.close()
       
# read in the currency exchange rates
# open file for reading
fh = open('currencyrates.txt')

# read the lines
records = fh.readlines()

# get 2 lists ready to store the info
currencies = []
rates = []

# loop through all the lines in the file
for record in records:
    # get rid of the trailing \n at the end of the file
    record = record.strip()

    # split the line into the parts
    currency, rate = record.split(',')

    # add the currency and rate to the lists
    currencies.append(currency)

    # turn the rate back to an float
    rate = float(rate)
    rates.append(rate)

currency_index_max = len(currencies)-1

# main program loop
while True:

    menu = 99
    # display main menu
    print("Select option:")
    print("0: Convert from British Pounds")
    print("1: Convert to British Pounds")
    print("2: Change an exchange rate")
    print("3: Save exchange rates and exit program")

    # get user input and check if valid
    while menu < 0 or menu > 3:
        try:
            menu = int(input("Enter option (0-3): "))
            if menu < 0 or menu > 3:
                print("Invalid option!")
        except:
            print("Invalid option!")

    # menu 0: convert from British Pounds
    if menu == 0:
        # display currency list
        print("Select currency to convert to:")
        currency_index = display_currency_menu()

        # get amount to convert
        while True:
            try:
                amount = int(input("Enter amount to convert: "))
                break
            except:
                print("Invalid input, try again.")

        # convert currency and display
        converted_amount = round(amount * rates[currency_index], 2)
        print(str(amount) + " British Pounds equals " + str(converted_amount) + " " + currencies[currency_index])
        input("Press Enter to continue")

    # menu 1: convert to British Pounds
    elif menu == 1:
        print("Select currency to convert from:")
        currency_index = display_currency_menu()

        # get amount to convert
        while True:
            try:
                amount = int(input("Enter amount to convert: "))
                break
            except:
                print("Invalid input, try again.")

        # convert currency and display
        converted_amount = round(amount / rates[currency_index], 2)
        print(str(amount) + " " + currencies[currency_index] + " equals " + str(converted_amount) + "British Pounds")
        input("Press Enter to continue")

    # menu 2: change exchange rate
    elif menu == 2:
        print("Select currency to change rate of:")
        currency_index = display_currency_menu()

        # display current rate and get new rate
        print(currencies[currency_index] + " current rate is: " + str(rates[currency_index]))
        while True:
            try:
                new_rate = float(input("Enter new rate: "))
                break
            except:
                print("Invalid input, try again.")

        # update rate
        rates[currency_index] = new_rate                                

        # write exchange rates to file in case of program crash
        file_write()
        print("Exchange rate updated and data saved to file")
        input("Press Enter to continue")

    # menu 3: write data to file and exit
    else:
        print("Saving exchange rate data to file")
        file_write()
        break

# exit program
print("Program exiting")
