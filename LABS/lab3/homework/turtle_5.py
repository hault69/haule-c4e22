from turtle import *
def draw_star(x,y,length):
    penup()
    setx(x)
    sety(y)
    pendown()
    for i in range(5):
        right(144)
        forward(length)      

draw_star(x = 10, y = 10, length = 100)