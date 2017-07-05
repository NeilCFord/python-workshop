# import modules
import random

# initialize variables
loops = 1
correct = 0

# ask users name
name = input("What is your name? ")

# main loop
while loops < 11:

    # generate random numbers
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    opr = random.randint(1,3)

    # if opr = 1, do addition
    if opr == 1:
        print("Question " + str(loops))
        print(str(num1) + " + " + str(num2) + "?")
        answer = num1 + num2

    # if opr = 2, do subtraction
    elif opr == 2:
        print("Question " + str(loops))
        print(str(num1) + " - " + str(num2) + "?")
        answer = num1 - num2

    # if opr = 3, do multiplication
    else:
        print("Question " + str(loops))
        print(str(num1) + " * " + str(num2) + "?")
        answer = num1 * num2

    # get answer from user
    guess = int(input())

    # is answer correct?
    if guess == answer:
        print("Correct!")
        correct = correct + 1
    else:
        print("Wrong!")

    # increase loop count
    loops = loops + 1

# print result
print(str(name) + ", you got " + str(correct) + " answers right.")
