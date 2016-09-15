# BTEC Software Development Assignment 2016
# Sample Solution - NOT FOR DISTRIBUTION
# Neil Ford - neil.ford@cpdforteachers.com

# program to convert to and from British Pounds to a selection of
# foriegn currencies and to allow for the exchange rates to be
# changed and saved.

# import modules (if required)
import easygui as eg


# define functions
# display currency list and return selection
def display_currency_menu(box_msg):
    title = "Currency List"
    choice = eg.choicebox(box_msg, title, currencies)
    menu = currencies.index(choice)
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

###
# Main Program Code
###
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

    # display main menu
    title = "Main Menu"
    options = ["Convert from British Pounds", "Convert to British Pounds", "Change an exchange rate", "Save exchange rates and exit program"]
    msg = "Select option:"
    choice = eg.choicebox(msg, title, options)
    
    # handle cancel being pressed
    if choice == None:
        menu = 3
    else:
        menu = options.index(choice)

    # menu 0: convert from British Pounds
    if menu == 0:
        # display currency list
        msg = "Select currency to convert to:"
        currency_index = display_currency_menu(msg)

        # get amount to convert
        amount = eg.integerbox("Enter amount to convert", lowerbound=1, upperbound=10000)

        # convert currency and display
        converted_amount = round(amount * rates[currency_index], 2)
        eg.msgbox(str(amount) + " British Pounds equals " + str(converted_amount) + " " + currencies[currency_index])

    # menu 1: convert to British Pounds
    elif menu == 1:
        msg = "Select currency to convert from:"
        currency_index = display_currency_menu(msg)

        # get amount to convert
        amount = eg.integerbox("Enter amount to convert", lowerbound=1, upperbound=10000)

        # convert currency and display
        converted_amount = round(amount / rates[currency_index], 2)
        eg.msgbox(str(amount) + " " + currencies[currency_index] + " equals " + str(converted_amount) + "British Pounds")

    # menu 2: change exchange rate
    elif menu == 2:
        msg = "Select currency to change rate of:"
        currency_index = display_currency_menu(msg)

        # display current rate and get new rate
        msg = currencies[currency_index] + " current rate is: " + str(rates[currency_index]) + "\n\n" + "Enter the new rate"

        while True:
            try:
                new_rate = float(eg.enterbox(msg))
                break
            except:
                eg.msgbox("Invalid input, try again.")

        # update rate
        rates[currency_index] = new_rate

        # write exchange rates to file in case of program crash
        file_write()
        eg.msgbox("Exchange rate updated and data saved to file")

    # menu 3: write data to file and exit
    else:
        eg.msgbox("Saving exchange rate data to file")
        file_write()
        break

# exit program
eg.msgbox("Program exiting")
