#模組：從別的程式呼叫程式碼
import turtle
from shapes import polygon

t = turtle.Turtle()
s = turtle.Screen(400, 400)

polygon(50, 50 ,3)
polygon(-50, 50, 4)
polygon(-50, -50, 5)
polygon(50, -50, 6)
 









# turtle.penup()
# turtle.goto(50, 50)
# turtle.pendown()

# n = 3

# for i in range(n):#繪製n邊形
#     turtle.forward(100)
#     turtle.left(360/n)



# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)

# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)