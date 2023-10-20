import turtle
import random

leo = turtle.Turtle()
colors = ['green', 'blue', 'black', 'yellow', 'pink']

for c in range(90):
    color = random.choice(colors)
    leo.color(color)
    leo.forward(4)
    leo.right(4)