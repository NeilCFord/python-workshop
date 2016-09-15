# AQA 4512/1 – Practical Programming
# Scenario 4 - Traditional Application
# A Population Model
#
# Sample Solution - NOT FOR DISTRIBUTION
# Neil Ford - neil@neilcford.uk

#import modules (if required)
import os


# define initial values (in case user chooses to display them first)
juveniles_num = 0
adults_num = 0
seniles_num = 0
juveniles_surv_rate = 0
adults_surv_rate  = 0
seniles_surv_rate = 0
birth_rate = 0.0
num_generations = 0
total_population = 0
generation_values = []


# define functions
def save_file(savefile):
    # how many records do we have
    records = len(generation_values)

    # open the file for write
    fh = open(savefile, 'w')

    # loop through the records
    record = 0
    while record < records:
    # get the name and score from the lists
        f_juv, f_adu, f_sen, f_tot = generation_values[record]
        # write them to the file
        fh.write(str(record) + ',' + str(f_juv) + ',' + str(f_adu) + ',' + str(f_sen) + ',' + str(f_tot) + '\n')
        record = record + 1

    fh.close()
    print("File saved\n")


def integer_question(question_text):
    while True:
        try:
            answer = int(input(question_text))
            break
        except:
            print("Invalid input, try again.")

    return answer


def range_question(question_text, min_value, max_value):
    answer = 99
    while answer < min_value or answer > max_value:
        try:
            answer = float(input(question_text))
            if answer < min_value or answer > max_value:
                print("Invalid input, try again.")
        except:
            print("Invalid input, try again.")

    return answer


# main program loop
while True:

    menu = 99
    # display main menu
    print("Select option:")
    print("0: Set the Generation 0 values")
    print("1: Display Generation 0 values")
    print("2: Run the model")
    print("3: Export the data")
    print("4: Quit the program")

    menu =input("Enter option (0-4): ")

    if menu == "0":
        # set generation 0 values
        juveniles_num = integer_question("Enter starting number of juveniles (000s): ")
        adults_num = integer_question("Enter starting number of adults (000s): ")
        seniles_num = integer_question("Enter starting number of seniles (000s): ")
        juveniles_surv_rate = range_question("Enter juveniles survival rate: ", 0, 1)
        adults_surv_rate = range_question("Enter adults survival rate: ", 0, 1)
        seniles_surv_rate = range_question("Enter seniles survival rate: ", 0, 1)

        birth_rate = 0
        while birth_rate <= 0:
            try:
                birth_rate = float(input("Enter birth rate: "))
                if birth_rate <= 0:
                    print("Invalid input, try again.")
            except:
                print("Invalid input, try again.")

        num_generations = int(range_question("Enter number of generations to model (5 - 25): ", 5, 25)) 

        # add input values to generations list
        total_population = juveniles_num + adults_num + seniles_num
        generation_values.append([juveniles_num, adults_num, seniles_num, total_population])

    elif menu == "1":
        # display generation 0 values
        print()
        print("Generation 0 values")
        print("No of Juveniles (1000s): " + str(juveniles_num))
        print("No of Adults (1000s): " + str(adults_num))
        print("No of Seniles (1000s): " + str(seniles_num))
        print("Juveniles Survival Rate: " + str(juveniles_surv_rate))
        print("Adults Survival Rate: " + str(adults_surv_rate))
        print("Seniles Survival Rate: " + str(seniles_surv_rate))
        print("Birth Rate: " + str(birth_rate) + "\n")

    elif menu == "2":
        # run model
        if num_generations > 0: # run only if generation 0 values have been enetered
            print()
            print("Running model...\n")
            # print headers and Generation 0 values
            juveniles_num, adults_num, seniles_num, total_population = generation_values[0]
            print("Generation     Juveniles     Adult     Seniles     Total")
            print("{:>8}{:>14}{:>12}{:>11}{:>11}".format(0, juveniles_num, adults_num, seniles_num, total_population))


            # iterate through generations
            for i in range(1,num_generations + 1):
                juveniles_num, adults_num, seniles_num, total_population = generation_values[i-1]

                new_juveniles_num = int((adults_num * birth_rate))               
                new_adults_num = int((juveniles_num * juveniles_surv_rate))
                new_seniles_num = int(((seniles_num * seniles_surv_rate) + (adults_num * adults_surv_rate)))
                new_total_population = new_juveniles_num + new_adults_num + new_seniles_num
                
                generation_values.append([new_juveniles_num, new_adults_num, new_seniles_num, new_total_population])
                print("{:>8}{:>14}{:>12}{:>11}{:>11}".format(i, new_juveniles_num, new_adults_num, new_seniles_num, new_total_population))

            print()

        else: # no generation 0 values entered
            print()
            print("You need to enter some Generation 0 values first!")
            print()

    elif menu == "3":
        # export data
        if num_generations > 0: # run only if generation 0 values have been enetered
            while True:  # run until data is saved
                filename = ""
                # get filename
                while filename == "":
                    filename = input("Enter file name to save data to (extension of .csv will be added automatically): ")
                    if filename == "":
                        print("Filename cannot be blank. Please input a valid filename.")

                # check if filename exists
                filename += ".csv"
                if os.path.isfile(filename):
                    # file exists
                    print(filename) # placeholder
                    choice = ""
                    while choice != "y" and choice != "n":
                        choice = input("File exists. Overwrite file? (y/n): ").lower()
                        if choice != "y" and choice != "n":
                            print("Invalid input, try again.")

                    if choice == "y":  # overwrite file
                        print("Overwriting file!")
                        save_file(filename)
                        break
                    else:
                        print("Data not saved.\n")
                        
                else:
                    # file does not exist, save data
                    save_file(filename)
                    break
            
        else: # no generation 0 values entered
            print()
            print("You need to enter some Generation 0 values first!")
            print()

    elif menu == "4":
        # exit program
        print("Program exiting...")
        break
        
    else:
        # invalid value entered
        print("Invalid input!")
        print()
        
