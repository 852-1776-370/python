from turtle import *
speed(0)
hideturtle()
for i in range(80):
    color("red")
    circle(i)
    color("orange")
    circle(i*0.8)
    color("purple")
    rt(5)
    fd(3)
