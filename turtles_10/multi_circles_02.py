# draw a multi circles using turtles
# from turtle module import Turtle, Screen classes
import random
from turtle import Turtle, Screen

# create a turtle object from Turtle class ( my_turtle )
my_turtle = Turtle()
my_turtle.speed('fast')

colors_list = ['red', 'blue', 'green', 'black', 'yellow', 'brown']

for i in range(20):
    chosen_color = random.choice(colors_list)
    my_turtle.color(chosen_color)
    my_turtle.circle(100)
    my_turtle.left(15)


my_screen = Screen()
my_screen.exitonclick()