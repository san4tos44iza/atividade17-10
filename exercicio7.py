import turtle

leo = turtle.Turtle()
leo.color('green')

for _ in range(4):
    leo.left(90)
    leo.backward(150)

leo.backward(80)
leo.backward(170)
leo.right(90)

for _ in range(3):
  leo.forward(150)
  leo.left(90)