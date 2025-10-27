import turtle
t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen()
screen.setup(width = 800 , height = 800)
offset = 100

def plotPoints(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.dot(5)
def drawCordPlane(xInterval,yInterval):
    t.hideturtle()
    t.penup()
    t.goto(300,-300)
    t.pendown()
    t.write('Time')
    t.goto(-300,-300)
    t.goto(-300,300)
    t.write('Money')
    for i in range(12):
        intervalCreatorY(-300,i*50-250,yInterval*(i+1))
    for i in range(12):
        intervalCreatorX(i*50-250,-300,xInterval*(i+1))
    screen.mainloop()
def intervalCreatorY(x,y,yInterval):
    t.goto(x,y)
    t.goto(x-10,y)
    t.write(yInterval, move=True)
    t.goto(x+625,y)
    t.goto(x,y)
def intervalCreatorX(x,y,xInterval):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(x,y-10)
    t.penup()
    t.goto(x,y-30)
    t.pendown()
    t.write(xInterval, align='center')
    t.penup()
    t.goto(x,y-10)
    t.pendown()
    t.goto(x,y+625)
    t.goto(x,y)
