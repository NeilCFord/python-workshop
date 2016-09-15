# A primary school teacher wants a computer program to test the basic
# arithmetic skills of her students. The program should generate a
# quiz consisting of a series of random questions, using in each case
# any two numbers and addition, subtraction and multiplication. The system
# should ask the student’s name, then ask 10 questions, output if the
# answer to each question is correct or not and produce a final score
# out of 10.

# import modules (if required)
import random

# define variables
score = 0
loops = 0

# Ask pupil's name
name = input("What is your name? ")

# main loop
# ask 10 questions
while loops < 10:
    loops = loops + 1

    # generate random numbers and question type
    numb1 = random.randint(1,10)
    numb2 = random.randint(1,10)

    question_type = random.randint(1,3)

    # print question number
    print("Question " + str(loops))
    
    # ask question
    # 1 = addition
    if question_type == 1:

        answer = numb1 + numb2
        
        while True:  # handles non-integar input
            try:
                guess = int(input("What is " + str(numb1) + " + " + str(numb2) + " ? "))
                break
            except:
                print("Invalid input, try again.")

    # 2 = subtraction
    elif question_type == 2:

        answer = numb1 - numb2

        while True:  # handles non-integar input
            try:
                guess = int(input("What is " + str(numb1) + " - " + str(numb2) + " ? "))
                break
            except:
                print("Invalid input, try again.")

    # 3 = multiplication
    else:

        answer = numb1 * numb2

        while True:  # handles non-integar input
            try:
                guess = int(input("What is " + str(numb1) + " * " + str(numb2) + " ? "))
                break
            except:
                print("Invalid input, try again.")

    # check answer, print "Correct" or "Wrong" and increase score
    if guess == answer:
        print("Correct!")
        score = score + 1
    else:
        print("Wrong!")

# print out total score
print(name + ", you got " + str(score) + " answers correct.")
