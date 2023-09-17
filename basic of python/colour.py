import turtle
colors=['orange','red','pink','yellow','blue','green']
screen=turtle.Screen()
trtl=turtle.Turtle()
trtl.speed(10)
trtl.colour(b"lue")
for x in range(120):
    trtl.pencolour(colors[x%76])
    trtl.width(x/5+8)
    trtl.forward(x)
    trtl.left(120)
    
  
