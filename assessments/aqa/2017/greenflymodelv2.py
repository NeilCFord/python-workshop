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
generation_values.append([juveniles_num, adults_num, seniles_num, total_population])


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
        while True:
            try:
                juveniles_num = int(input("Enter starting number of juveniles (000s): "))
                break
            except:
                print("Invalid input, try again.")

        while True:
            try:
                adults_num = int(input("Enter starting number of adults (000s): "))
                break
            except:
                print("Invalid input, try again.")

        while True:
            try:
                seniles_num = int(input("Enter starting number of seniles (000s): "))
                break
            except:
                print("Invalid input, try again.")

        juveniles_surv_rate = 99
        while juveniles_surv_rate < 0 or juveniles_surv_rate > 1:
            try:
                juveniles_surv_rate = float(input("Enter juveniles survival rate: "))
                if juveniles_surv_rate < 0 or juveniles_surv_rate > 1:
                    print("Invalid input, try again.")
            except:
                print("Invalid input, try again.")

        adults_surv_rate = 99
        while adults_surv_rate < 0 or adults_surv_rate > 1:
            try:
                adults_surv_rate = float(input("Enter adults survival rate: "))
                if adults_surv_rate < 0 or adults_surv_rate > 1:
                    print("Invalid input, try again.")
            except:
                print("Invalid input, try again.")

        seniles_surv_rate = 99
        while seniles_surv_rate < 0 or seniles_surv_rate > 1:
            try:
                seniles_surv_rate = float(input("Enter seniles survival rate: "))
                if seniles_surv_rate < 0 or seniles_surv_rate > 1:
                    print("Invalid input, try again.")
            except:
                print("Invalid input, try again.")

        birth_rate = 0
        while birth_rate <= 0:
            try:
                birth_rate = float(input("Enter birth rate: "))
                if birth_rate <= 0:
                    print("Invalid input, try again.")
            except:
                print("Invalid input, try again.")

        num_generations = 99
        while num_generations < 5 or num_generations > 25:
            try:
                num_generations = int(input("Enter number of generations to model: "))
                if num_generations < 5 or num_generations > 25:
                    print("Invalid input, try again.")
            except:
                print("Invalid input, try again.")

        # print(juveniles_num, adults_num, seniles_num, juveniles_surv_rate, adults_surv_rate, seniles_surv_rate, birth_rate, num_generations)

        # add input values to generations list
        total_population = juveniles_num + adults_num + seniles_num
        generation_values[0] = [juveniles_num, adults_num, seniles_num, total_population]
        print (generation_values)


    elif menu == "1":
        # display generation 0 values
        print("")
        print("Generation 0 values")
        print("No of Juveniles (1000s):", juveniles_num)
        print("No of Adults (1000s): " + str(adults_num))
        print("Juveniles Survival Rate: " + str(juveniles_surv_rate))
        print("Birth Rate:", birth_rate)

        print("")        

    elif menu == "2":
        # run model
        if num_generations > 0: # run only if generation 0 values have been enetered
            print("")
            print("Running model...")
            print()
            # print table headers and Generation 0 values
            print("Generation    Juveniles    Adult    Seniles    Total")
            print()
            juveniles_num, adults_num, seniles_num, total_population = generation_values[0]
            print("    {}           {}          {}        {}        {}".format(0,juveniles_num, adults_num, seniles_num, total_population))
            print()

            # iterate through generations
            for i in range(1,num_generations + 1):
                juveniles_num, adults_num, seniles_num, total_population = generation_values[i-1]

                new_juveniles_num = int((adults_num * birth_rate))               
                new_adults_num = int((juveniles_num * juveniles_surv_rate))
                new_seniles_num = int(((seniles_num * seniles_surv_rate) + (adults_num * adults_surv_rate)))
                new_total_population = new_juveniles_num + new_adults_num + new_seniles_num
                
                generation_values.append([new_juveniles_num, new_adults_num, new_seniles_num, new_total_population])
                print("    {}           {}          {}        {}        {}".format(i,new_juveniles_num, new_adults_num, new_seniles_num, new_total_population))
                print()

        else: # no generation 0 values entered
            print("")
            print("You need to enter some Generation 0 values first!")
            print("")

    elif menu == "3":
        # export data
        if num_generations > 0: # run only if generation 0 values have been enetered
            # get filename
            filename = ""
            while filename == "":
                filename = input("Enter file name to save data to (extension of .csv will be added automatically): ")
                if filename == "":
                    print("Filename cannot be blank. Please input a valid filename.")

            # check if filename exists
            filename += ".csv"
            if os.path.isfile(filename):
                # file exists
                print(filename) # placeholder

            else:
                # file does not exist, save data
                save_file(filename)
            

        else: # no generation 0 values entered
            print("")
            print("You need to enter some Generation 0 values first!")
            print("")

    elif menu == "4":
        # exit program
        print("Program exiting...")
        break
        
    else:
        # invalid value entered
        print("Invalid input!")
        print("")
        
