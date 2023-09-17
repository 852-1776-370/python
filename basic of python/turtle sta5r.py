from turtle import *
#loadWindow =turtle.Screen()
speed(100)
color("red","pink")
begin_fill()
for i in range(10,100,10):
    circle(1*i)
    circle(-1*i)
    right(i)
end_fill()
exitonclick()

