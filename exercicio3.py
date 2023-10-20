import turtle

leo = turtle.Turtle()
leo.shape('triangle')
leo.pensize(5)


for color in ['pink', 'red', 'black', 'blue']:
    leo.color(color)
    leo.forward(150)
    leo.right(90)
leo.penup()
leo.forward(200)
leo.pendown()
for color in ['pink', 'red', 'black', 'blue']:
    leo.color(color)
    leo.forward(150)
    leo.right(90)