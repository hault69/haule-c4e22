from turtle import *
def draw_square(length,colors):
    colors = "red"
    for i in range(4):
        color(colors)
        forward(length)
        left(90)