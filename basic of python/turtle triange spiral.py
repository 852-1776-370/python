from turtle import *
bgcolor('pink')
color("yellow","red")
begin_fill()
speed(1000)
for i in range(100):
    forward(i*5)
    left(120)
up()
goto(0,0)
down()
for i in range(100):
    fd(i*5)
    rt(120)
end_fill()   
