import turtle

leo = turtle.Turtle()

for _ in range(4):
    leo.shape('circle')
    leo.color('green')
    leo.forward(100)
    leo.right(90)

leo.penup()
leo.forward(150)
leo.right(90)

for _ in range(4):
   leo.pendown()
   leo.shape('turtle')
   leo.color('pink')
   leo.left(90)
   leo.forward(100)

leo.penup()
leo.forward(150)
leo.right(90)

for _ in range(4):
    leo.pendown()
    leo.shape('triangle')
    leo.color('purple')
    leo.left(90)
    leo.forward(100)

leo.penup()
leo.forward(300)
leo.right(90)

for _ in range(4):
    leo.pendown()
    leo.shape('square')
    leo.color('red')
    leo.right(90)
    leo.forward(100)

leo.penup()
leo.forward(30)
leo.left(90)

for _ in range(3):
    leo.pendown()
    leo.shape('square')
    leo.color('black')
    leo.right(90)
    leo.forward(400)

leo.forward(150)
leo.right(90)
leo.forward(400)
leo.right(90)
leo.forward(150)
