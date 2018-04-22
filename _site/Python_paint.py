import random
import turtle
from time import sleep

def main():
    tlist = []
    head = 0
    numturtles = 10
    for i in range(numturtles):
        nt = turtle.Turtle() # Make a new turtle, initialize values
        nt.setheading(head)
        nt.pensize(2)
        #nt.color(random.randrange(256), random.randrange(256), random.randrange(256))
        nt.speed(10)
        nt._tracer(30, 0)
        tlist.append(nt)
        head = head + 360 / numturtles

    for i in range(100):
        moveturtles(tlist, 15, i)

    w = tlist[0]
    w.up()
    w.goto(-130, 40)
    w.write("Hello World", True, "center", "30px")
    w.goto(-130, -35)
    w.write("Computer Science", True, "center", "30px")
    w.isvisible()

def moveturtles(turtlelist, dist, angle):
    for turtle in turtlelist: #Make every turtle on the list do the same aactions
        turtle.forward(dist)
        turtle.right(angle)

main()  