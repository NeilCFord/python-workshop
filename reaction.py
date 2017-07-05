import random
import time

total_time = 0
loops = 0

while loops < 3:

    #pick a random number and store in sleep_time
    sleep_time = random.randint(3, 7)

    #sleep for sleep_time seconds
    time.sleep(sleep_time)

    #print "GO!"
    print("Go!")

    #store the current time in start_time
    start_time = time.time()

    #wait for subject to press keyboard
    input()

    #work out how long they took by subtracting the start_time now from the time now
    result = time.time() - start_time
    
    #print out how long they took
    print(result)
    
    total_time = total_time + result
    loops = loops + 1

print("Your average time was: " + str(total_time/3))
