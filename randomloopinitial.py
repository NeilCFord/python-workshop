from turtle import *
import random

speed(3)
colormode(255)

loops = 0

def choosecolour():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    colour = (red, green, blue)
    return colour

left(90)

while loops < 20:

    pencolor(choosecolour())
       
    forward(100)
    right(145)
    pencolor(choosecolour())
    forward(120)
    left(145)
    pencolor(choosecolour())
    forward(100)
    right(97)
    loops = loops + 1


