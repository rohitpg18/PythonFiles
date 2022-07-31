import turtle

ninja = turtle.Turtle()

ninja.speed(588)

for i in range (50):
    ninja.forward(200)
    ninja.right(10)
    ninja.forward(100)
    ninja.left(10)
    ninja.forward(10)
    ninja.right(30)

    ninja.penup()
    ninja.setposition(0,1)
    ninja.pendown()

    ninja.right(2)

turtle.done()