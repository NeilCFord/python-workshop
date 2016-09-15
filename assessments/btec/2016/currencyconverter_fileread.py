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

# print the data
for i in range(len(currencies)):
    print (i, currencies[i], rates[i])

print(currencies)
print(rates)
    
