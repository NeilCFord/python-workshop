# import modules (if required)

# define variables
pupils = {}  # empty dictionary to receive file contents
choice = 0

# ask which class
while choice < 1 or choice > 3:
    try:
        choice = int(input("Which class do you want to work with? (1-3) "))
        if choice < 1 or choice > 3:
            print("Invalid choice, please try again")
    except:
        print("Invalid choice, please try again")

# debug output
print(choice)

# read appropriate class file

file_name = "class" + str(choice) + "_scores.txt"

# open file for reading
fh = open(file_name)

# read the lines
records = fh.readlines()

# loop through all the lines in the file
for record in records:
    # get rid of the trailing \n at the end of the file
    record = record.strip()

    # split the line into the parts
    name, score = record.split(',')

    # add name and score to pupils dictionary
    pupils[name] = int(score)

# debug output
print(pupils)
for pupil, score in pupils.items():
    print(pupil, score)

# main loop
while True:

    # ask pupil name
    pupil = input("Enter pupil's name (or exit to finish): ")

    if pupil == "exit":
        break

    score = 99
    # ask score
    while score < 0 or score > 10:
        try:
            score = int(input("Enter quiz score (0-10): "))
            if score < 0 or score > 10:
                print("Invalid input, please try again")
        except:
            print("Invalid input, please try again")

    # debug output
    print(pupil, score)

    # add name and score to class list
    pupils[pupil] = score

    # debug output
    print(pupils)

# on exit, save class file
# open the file for writing
fh = open(file_name, 'w')

# loop through the records
for pupil, score in pupils.items():

    # write each pupil to the file
    fh.write(pupil + ',' + str(score) + '\n')

# close file
fh.close()

# exit program
print("Program exiting")
