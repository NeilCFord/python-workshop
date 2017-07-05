import time
import random
import easygui as eg

score = 0

loops = 0

while loops < 10:
    loops = loops + 1
    numb1 = random.randint(1,10)
    numb2 = random.randint(1,10)

    question_type = random.randint(1,3)

    if question_type == 1:

        answer = numb1 + numb2
    
##        print("Question " + str(loops))
##        guess = int(input("What is " + str(numb1) + " + " + str(numb2) + " ? "))
        guess = eg.integerbox("What is " + str(numb1) + " + " + str(numb2) + " ? ", title = "Question " + str(loops))

    elif question_type == 2:

        answer = numb1 - numb2

        # avoid negative results
##        if numb2 > numb1:
##            answer = numb2 - numb1
##            guess = eg.integerbox("What is " + str(numb2) + " - " + str(numb1) + " ? ", title = "Question " + str(loops))
##        else:
##            answer = numb1 - numb2
##            guess = eg.integerbox("What is " + str(numb1) + " - " + str(numb2) + " ? ", title = "Question " + str(loops))

##        print("Question " + str(loops))
##        guess = int(input("What is " + str(numb1) + " - " + str(numb2) + " ? "))
        guess = eg.integerbox("What is " + str(numb1) + " - " + str(numb2) + " ? ", title = "Question " + str(loops), lowerbound=-9, upperbound=100)


    else:

        answer = numb1 * numb2

##        print("Question " + str(loops))
##        guess = int(input("What is " + str(numb1) + " * " + str(numb2) + " ? "))
        guess = eg.integerbox("What is " + str(numb1) + " * " + str(numb2) + " ? ", title = "Question " + str(loops))


    if guess == answer:
        #print("Correct!")
        eg.msgbox("Correct")
        score = score + 1
    else:
        #print("Wrong!")
        eg.msgbox("Wrong!")

#print("You got " + str(score) + " answers correct.")
eg.msgbox("You got " + str(score) + " answers correct.", title="Game Over")
