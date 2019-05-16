import turtle

t1 = turtle.Turtle(shape="turtle")
t2 = turtle.Turtle(shape="turtle")

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
SIDE = 50

X_COR = -200
Y_COR = 200

y_count = 0

#setup turtle1
t1.penup()
t1.speed(0)
t1.setpos(X_COR,Y_COR)
t1.setheading(RIGHT)
t1.fillcolor('black')

#setup turtle2
t2.penup()
t2.hideturtle()
t2.speed(0)
t2.setpos(X_COR,Y_COR)
t2.setheading(RIGHT)

def box(t1):
    t1.pendown()
    t1.forward(SIDE)
    t1.seth(DOWN)
    t1.forward(SIDE)
    t1.seth(LEFT)
    t1.forward(SIDE)
    t1.seth(UP)
    t1.forward(SIDE)
    t1.setheading(RIGHT)

def whiteFirst(t1):
    for i in range(0, 8):
        box(t1)
        t1.forward(SIDE)
        if(i%2 == 0):
            t1.begin_fill()
        else:
            t1.end_fill()

def blackFirst(t1):
    for i in range(0, 8):
        t1.begin_fill()
        box(t1)
        t1.forward(SIDE)
        if i%2 == 0:
            t1.end_fill()
            
def lineReset(t1):
        t1.setx(X_COR)
        t1.sety(t1.ycor() - 50)

def loopyloop(t1):
    for i in range(0, 4):
        whiteFirst(t1)
        lineReset(t1)
        blackFirst(t1)
        lineReset(t1)
    t1.hideturtle()
    
def blueLoop(t2):
    t2.fillcolor('blue')
    for i in range(0, 4):
        blackFirst(t2)
        lineReset(t2)
        whiteFirst(t2)
        lineReset(t2)
    t2.hideturtle()

def redLoop(t2):
    t2.fillcolor('red')
    for i in range(0, 4):
        blackFirst(t2)
        lineReset(t2)
        whiteFirst(t2)
        lineReset(t2)
    t2.hideturtle()

def main():
    loopyloop(t1)
##    blueLoop(t2) #fills in the white with blue
##    redLoop(t2)  #fills in the white with red (checkers board)
main()
