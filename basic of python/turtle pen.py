from turtle import *
pensize(40)
pencolor("red")
fd(20)
pensize(40)
pencolor("yellow")
for i in range(6):
    up()
    goto(i*10,i*-40)
    down()
    fd(i*20)
