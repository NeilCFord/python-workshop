from turtle import *
import random

speed(3)

left(90)

loops = 0
colours = ["red", "blue", "green", "orange", "pink", "yellow", "purple"]

while loops < 20:

    chosen_colour = random.choice(colours)
    pencolor(chosen_colour)
       
    forward(100)
    right(145)
    chosen_colour = random.choice(colours)
    pencolor(chosen_colour)
    forward(120)
    left(145)
    chosen_colour = random.choice(colours)
    pencolor(chosen_colour)
    forward(100)
    right(97)
    loops = loops + 1


