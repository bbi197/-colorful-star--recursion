import turtle

a = turtle.Turtle()
a.getscreen().bgcolor("black")
a.penup()
a.goto(-200, 100)
a.pendown()
a.color("yellow")
a.speed(25)

def star(turtle, size):
    if size <= 10:
        return
    else:
        turtle.begin_fill()
        # Modified the loop range to 5 and changed the angle to 144 degrees
        for i in range(5):
            turtle.pensize(2)
            turtle.forward(size)
            # Changed the recursion call to use size/2 instead of size/3
            star(turtle, size/2)
            turtle.left(144)
        turtle.end_fill()

star(a, 360)
turtle.done()
