import turtle
turtle.shape('turtle')
turtle.speed(10)
n=40
while True:
    for i in range(4):
        turtle.forward(n + 20)
        turtle.left(90)
    turtle.penup()
    turtle.forward(n + 30)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(180)
    n+=20
    turtle.pendown()



