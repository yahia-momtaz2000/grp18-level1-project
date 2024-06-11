# draw a multi circles using turtles
# from turtle module import Turtle, Screen classes
import random
from turtle import Turtle, Screen

# create a turtle object from Turtle class ( my_turtle )
my_turtle = Turtle()


# draw a triangle = angle 60;
num_of_sides = 3
for i in range(num_of_sides):
    my_turtle.forward(100)
    my_turtle.left(360/num_of_sides)


my_screen = Screen()
my_screen.exitonclick()