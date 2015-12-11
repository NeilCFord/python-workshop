# open the file for read
fh = open("BFS_SpamIPs.txt", 'r')

# read all the lines into a list
lines = fh.readlines()

# close file
fh.close()

# strip newline characters
for i in range(len(lines)):
    lines[i] = lines[i].strip("\n")

# using a for loop, print the lines out
for line in lines:
    print(line)

# print out sorted list
sorted_lines = sorted(lines)
print("\nSorted IPs")
for line in sorted_lines:
    print(line)

# open the file for write
fh = open("BFS_SpamIPs.txt", 'w')

# write all the lines out to the file
for line in sorted_lines:
    fh.write(line+"\n")

# close file
fh.close()
