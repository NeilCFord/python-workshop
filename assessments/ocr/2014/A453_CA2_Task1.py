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
    numb1 = random.randint(1, 10)
    numb2 = random.randint(1, 10)

    question_type = random.randint(1, 3)

    # ask question
    # 1 = addition
    if question_type == 1:

        answer = numb1 + numb2
        question = "What is " + str(numb1) + " + " + str(numb2) + " ? "

    # 2 = subtraction
    elif question_type == 2:

        answer = numb1 - numb2
        question = "What is " + str(numb1) + " - " + str(numb2) + " ? "

    # 3 = multiplication
    else:

        answer = numb1 * numb2
        question = "What is " + str(numb1) + " * " + str(numb2) + " ? "

    # Print question number and question
    print("Question " + str(loops))
    guess = int(input(question))

    # check answer, print "Correct" or "Wrong" and increase score
    if guess == answer:
        print("Correct!")
        score = score + 1
    else:
        print("Wrong!")

# print out total score
print(name + ", you got " + str(score) + " out of " + str(loops) + " answers correct.")
