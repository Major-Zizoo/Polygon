import turtle

turtle.Screen().bgcolor("white")
turtle.Screen().setup(500,500)

pen=turtle.Turtle()
pen.color("aqua")
pen.width(7)

pen.begin_fill()
pen.fillcolor("blue")

for i in range(6):
    pen.forward(30)
    pen.right(60)

pen.end_fill()
turtle.done()
