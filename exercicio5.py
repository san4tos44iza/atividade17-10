import turtle

leo = turtle.Turtle()
leo.shape('arrow')
leo.color('purple')

for _ in [1, 2, 3]:
    leo.forward(90)
    leo.right(120)

leo = turtle.Turtle()
leo.shape('turtle')
leo.color('black')

for _ in [1, 2, 3, 4]:
    leo.forward(130)
    leo.right(90)