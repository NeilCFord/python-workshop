#import modules
import time, random

#display instructions
print()
print("Welcome to the Reaction Timer game")
time.sleep (0.5)
print ("When 'Go!' appears, press the Enter key as quickly as possible to record your reaction time")
print("Do this three times to get your average time")

#main program loop
loops = 0
total_time = 0
reaction_times = []

while loops < 3:

    #pick a random number and store in sleep_time
    #(set variable sleep_time equal to a random number)
    sleep_time = random.randint(3,8)

    #sleep for sleep_time seconds
    time.sleep(sleep_time)

    #print "GO!"
    print("Go!")

    #store the current time in start_time
    #(set variable start_time equal to current time)
    start_time = time.time()

    #wait for subject to press keyboard
    input()

    #work out how long they took by subtracting the start_time now from the time now

    result = time.time() - start_time
    reaction_times.append(result)

    #print out how long they took
    print("Reaction time: " + str(round(result,2)) + " seconds")

    total_time = total_time + result
    loops = loops + 1

#print out fastest time
fastest_time = 99
for i in reaction_times:
    if i < fastest_time:
        fastest_time = i

print()
print("Your fastest time was: " + str(round(fastest_time, 2)) + " seconds")

#print out average time taken
print("Your average time was: " + str(round(total_time/loops, 2)) + " seconds")
