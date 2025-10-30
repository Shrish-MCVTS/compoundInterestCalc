import turtle
# Turtle graphics module to plot points and draw coordinate plane
origin = (-300, -300)
STEP = 50
# Function to plot points on the graph
def plotPoints(x,y,nX,nY,t):
    t.penup()
    wX, wY = convertToGraphCords(x, y,nX,nY)
    t.goto(wX, wY)
    t.pendown()
    t.dot(10)
# Function to convert graph coordinates to turtle screen coordinates
def convertToGraphCords(graphX,  graphY,GRAPH_STEP_X,GRAPH_STEP_Y):
    x = origin[0] + (graphX * (STEP/GRAPH_STEP_X))
    y = origin[1] + (graphY * (STEP/GRAPH_STEP_Y))
    return x, y  
# Function to draw the coordinate plane
def drawCordPlane(xInterval,yInterval, t):
    t.hideturtle()
    t.penup()
    t.goto(300,-300)
    t.pendown()
    t.write('Time(years)')
    t.goto(-300,-300)
    t.goto(-300,300)
    t.write('Money($)')
    for i in range(12):
        intervalCreatorY(-300,i*50-250,yInterval*(i+1) , t)
    for i in range(12):
        intervalCreatorX(i*50-250,-300,xInterval*(i+1) , t)
# Function to create intervals on the axes
def intervalCreatorY(x,y,yInterval , t):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(x-10,y)
    t.penup()
    t.goto(x-30,y)
    t.pendown()
    t.write(yInterval, align='center')
    t.penup()
    t.goto(x-10,y)
    t.pendown()
    t.goto(x+625,y)
    t.goto(x,y)

def intervalCreatorX(x,y,xInterval , t):
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
