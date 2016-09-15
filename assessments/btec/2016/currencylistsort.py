# open the file for read
fh = open("currencyrates.txt", 'r')

# read all the lines into a list
lines = fh.readlines()

# close file
fh.close()

# using a for loop, print the lines out
for line in lines:
    print(line)

# print out sorted list
sorted_lines = sorted(lines)
print("\nSorted currencies")
for line in sorted_lines:
    print(line)

# open the file for write
fh = open("currencyrates.txt", 'w')

# write all the lines out to the file
for line in sorted_lines:
    fh.write(line)

# close file
fh.close()
