# now we'll read the data back in
fh = open('csv.txt')
# read the lines
records = fh.readlines()
# get 2 lists ready to store the info
names = []
scores = []
# loop through all the lines in the file
for record in records:
    # get rid of the trailing \n at the end of the file
    record = record.strip()

    # split the line into the parts
    name, score = record.split(',')

    # add the name and score to the lists
    names.append(name)

    # turn the score back to an integer
    score = int(score)
    scores.append(score)

# print the data
print(names)
print(scores)
