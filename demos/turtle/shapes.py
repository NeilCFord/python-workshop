# import libraries
import turtle

# create turtle drawing palette
t = turtle.Pen()

# define function to draw shape
def draw_shape():

    # calculate start position
    start_x = x - (size/2)
    start_y = y - (size/2)

    # set pen up
    t.up()

    # move to start position
    t.goto(start_x, start_y)

    # draw shape
    t.down()
    t.setheading(0)
    for i in range(sides):
        t.forward(size)
        t.left(360/sides)

# open file
fh = open("file.txt", 'r')

# read the lines
records = fh.readlines()

# using a for loop, break each line down
for record in records:

    # get rid of the trailing \n at the end of the file
    record = record.strip()

    # split the line into the parts
    x, y, sides, size = record.split(',')

    #turn integers back into integers
    x = int(x)
    y = int(y)
    sides = int(sides)
    size = int(size)

    # draw shape
    draw_shape()

fh.close()


