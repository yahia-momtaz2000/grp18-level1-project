# from turtle module import Turtle, Screen classes
from turtle import Turtle, Screen


# create a turtle object from Turtle class ( my_turtle )
my_turtle = Turtle()

my_turtle.shape('turtle')
my_turtle.color('black')
my_turtle.fillcolor('green')

my_turtle.begin_fill()
for i in range(2):
    my_turtle.forward(250)
    my_turtle.left(90) # angle  90
    my_turtle.forward(200)
    my_turtle.left(90)  # angle  90
my_turtle.end_fill()

my_turtle.penup() # do not draw a line
my_turtle.goto(-200, 100)
my_turtle.shape('square')
my_turtle.stamp()

for i in range(2):
    my_turtle.forward(100)
    my_turtle.stamp()
# draw a circle
my_turtle.shape('turtle')
my_turtle.goto(-100, -200)
my_turtle.pendown()
my_turtle.circle(50)



# create a screen object from Screen class ( my_screen )
my_screen = Screen()
my_screen.exitonclick()