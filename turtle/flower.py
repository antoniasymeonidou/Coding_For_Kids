import turtle

def petal():
    turtle.speed(0)
    turtle.width(5)
    turtle.begin_fill()
    turtle.color('crimson')
    turtle.circle(150, 60)
    turtle.left(120)
    turtle.circle(150, 60)
    turtle.end_fill()

for i in range(20):
    petal()
    turtle.left(360 / 20)

turtle.done()
