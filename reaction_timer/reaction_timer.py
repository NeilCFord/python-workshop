#import modules
import time, random

#pick a random number and store in sleep_time
#(set variable sleep_time equal to a random number)
sleep_time = random.randint(3,8)

#sleep for sleep_time seconds
time.sleep(sleep_time)

#print "GO!"
print("Go")

#store the current time in start_time
#(set variable start_time equal to current time)
start_time = time.time()

#wait for subject to press keyboard
input()

#work out how long they took by subtracting the start_time now from the time now

result = time.time() - start_time

#print out how long they took
print(result)
