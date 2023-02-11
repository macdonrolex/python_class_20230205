import turtle
def polygon(x, y, n):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    for i in range(n):#繪製n邊形
        turtle.forward(100)
        turtle.left(360/n)