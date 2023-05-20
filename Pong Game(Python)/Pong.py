import turtle
import winsound
import random
import datetime

window = turtle.Screen()                    #Set the Screen as window
window.title("Pong by @Jiaming Guan")       #The Screen title
window.bgcolor("black")                     #Set the background color of the Screen
window.setup(width=800, height=600)
window.tracer(0)                             #Stops the window from updating

#Score
score_a = 0
score_b = 0

#Skill ColdDown
ColdDown_a_up = 0        #At the beginning
ColdDown_a_down = 0
ColdDown_b_up = 0
ColdDown_b_down = 0
    
#Paddle A
paddle_a = turtle.Turtle()                  #Turtle() is the class name
paddle_a.speed(0)                           #Sets it to the maximum speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)        #Height times 5, width * 1
paddle_a.penup()                            #Don't draw a line as it move
paddle_a.goto(-350, 0)                      #Stay at left side of the screen

#Paddle B
paddle_b = turtle.Turtle()                  #Turtle() is the class name
paddle_b.speed(0)                           #Sets it to the maximum speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)        #Height times 5, width * 1
paddle_b.penup()                            #Don't draw a line as it move
paddle_b.goto(350, 0)                       #Stay at left side of the screen

#Ball
ball = turtle.Turtle()                  #Turtle() is the class name
ball.speed(0)                           #Sets it to the maximum speed
ball.shape("square")
ball.color("white")
ball.penup()                            #Don't draw a line as it move
ball.goto(0, 0)                         #Stay at left side of the screen
ball_direction = random.randint(1,4)
if(ball_direction == 1):
    ball.dx = 0.1                             #Everytime the ball move, it move by 0.1 pixle(x)
    ball.dy = 0.1                             #Everytime the ball move, it move by 0.1 pixle(y)
elif(ball_direction == 2):
    ball.dx = -0.1
    ball.dy = 0.1
elif(ball_direction == 3):
    ball.dx = 0.1
    ball.dy = -0.1
else:
    ball.dx = -0.1
    ball.dy = -0.1

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#Player A Skill
#Skill C
A_skill_C = turtle.Turtle()
A_skill_C.speed(0)
A_skill_C.color("white")
A_skill_C.hideturtle()
A_skill_C.shapesize(stretch_wid=2, stretch_len=2)
A_skill_C.penup()
A_skill_C.goto(-300, -280)
A_skill_C.write("C", align="center", font=("Courier", 14, "normal"))

A_Box_C = turtle.Turtle()
A_Box_C.speed(0)                           
A_Box_C.shape("square")
A_Box_C.color("white")
A_Box_C.shapesize(stretch_wid=2, stretch_len=2)        
A_Box_C.penup()                            
A_Box_C.goto(-300, -240)     

#Skill V
A_skill_V = turtle.Turtle()
A_skill_V.speed(0)
A_skill_V.color("white")
A_skill_V.hideturtle()
A_skill_V.shapesize(stretch_wid=2, stretch_len=2)
A_skill_V.penup()
A_skill_V.goto(-250, -280)
A_skill_V.write("V", align="center", font=("Courier", 14, "normal"))

A_Box_V = turtle.Turtle()
A_Box_V.speed(0)                           
A_Box_V.shape("square")
A_Box_V.color("white")
A_Box_V.shapesize(stretch_wid=2, stretch_len=2)        
A_Box_V.penup()                            
A_Box_V.goto(-250, -240)

#Player B Skill
#Skill N
A_skill_N = turtle.Turtle()
A_skill_N.speed(0)
A_skill_N.color("white")
A_skill_N.hideturtle()
A_skill_N.shapesize(stretch_wid=2, stretch_len=2)
A_skill_N.penup()
A_skill_N.goto(250, -280)
A_skill_N.write("N", align="center", font=("Courier", 14, "normal"))

A_Box_N = turtle.Turtle()
A_Box_N.speed(0)                           
A_Box_N.shape("square")
A_Box_N.color("white")
A_Box_N.shapesize(stretch_wid=2, stretch_len=2)        
A_Box_N.penup()                            
A_Box_N.goto(250, -240)

#Skill M
A_skill_M = turtle.Turtle()
A_skill_M.speed(0)
A_skill_M.color("white")
A_skill_M.hideturtle()
A_skill_M.shapesize(stretch_wid=2, stretch_len=2)
A_skill_M.penup()
A_skill_M.goto(300, -280)
A_skill_M.write("M", align="center", font=("Courier", 14, "normal"))

A_Box_M = turtle.Turtle()
A_Box_M.speed(0)                           
A_Box_M.shape("square")
A_Box_M.color("white")
A_Box_M.shapesize(stretch_wid=2, stretch_len=2)        
A_Box_M.penup()                            
A_Box_M.goto(300, -240)

#Function
def paddle_a_up():
    y = paddle_a.ycor()                 #Set y = paddle_a's y coordinate
    y += 30                             #Change the coordinate
    paddle_a.sety(y)                    #Apply the change

def paddle_a_down():
    y = paddle_a.ycor()                 #Set y = paddle_a's y coordinate
    y -= 30                             #Change the coordinate
    paddle_a.sety(y)                    #Apply the change

def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)

def skill_c():
    global ColdDown_a_up
    global Skill_ready_a_up
    if(ColdDown_a_up == 0):
        y = paddle_a.ycor()
        y += 150
        paddle_a.sety(y)
        ColdDown_a_up = 5
        Skill_ready_a_up = datetime.datetime.now() + datetime.timedelta(0,5)

def skill_v():
    global ColdDown_a_down
    global Skill_ready_a_down
    if(ColdDown_a_down == 0):
        y = paddle_a.ycor()
        y += -150
        paddle_a.sety(y)
        ColdDown_a_down = 5
        Skill_ready_a_down = datetime.datetime.now() + datetime.timedelta(0,5)

def skill_n():
    global ColdDown_b_up
    global Skill_ready_b_up
    if(ColdDown_b_up == 0):
        y = paddle_b.ycor()
        y += 150
        paddle_b.sety(y)
        ColdDown_b_up = 5
        Skill_ready_b_up = datetime.datetime.now() + datetime.timedelta(0,5)

def skill_m():
    global ColdDown_b_down
    global Skill_ready_b_down
    if(ColdDown_b_down == 0):
        y = paddle_b.ycor()
        y += -150
        paddle_b.sety(y)
        ColdDown_b_down = 5
        Skill_ready_b_down = datetime.datetime.now() + datetime.timedelta(0,5)

window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")     #If the window detected s, call the function paddle_a_up
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")
window.onkeypress(skill_c, "c")
window.onkeypress(skill_v, "v")
window.onkeypress(skill_n, "n")
window.onkeypress(skill_m, "m")

#Main game loop
while True:
    window.update()

    #Skill ColdDown Check
    if(ColdDown_a_up == 5):
        A_Box_C.fillcolor("gray")
        A_Box_C.begin_fill()  
        if(datetime.datetime.now() > Skill_ready_a_up):
            ColdDown_a_up = 0
            A_Box_C.fillcolor("white")
            A_Box_C.begin_fill() 
    
    if(ColdDown_a_down == 5):
        A_Box_V.fillcolor("gray")
        A_Box_V.begin_fill()  
        if(datetime.datetime.now() > Skill_ready_a_down):
            ColdDown_a_down = 0
            A_Box_V.fillcolor("white")
            A_Box_V.begin_fill() 

    if(ColdDown_b_up == 5):
        A_Box_N.fillcolor("gray")
        A_Box_N.begin_fill()
        if(datetime.datetime.now() > Skill_ready_b_up):
            ColdDown_b_up = 0
            A_Box_N.fillcolor("white")
            A_Box_N.begin_fill()

    if(ColdDown_b_down == 5):
        A_Box_M.fillcolor("gray")
        A_Box_M.begin_fill()
        if(datetime.datetime.now() > Skill_ready_b_down):
            ColdDown_b_down = 0
            A_Box_M.fillcolor("white")
            A_Box_M.begin_fill()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)     #Ball's x coordinate + 0.1 everytime since ball.dx = 0.1
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290:               #The total ycor is (300 and -300)
        ball.sety(290)                  #Prevent it from going outside the screen
        ball.dy *= -1.05                #Reverse the direction of the ball and make it bounce down(Add some speed)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1.05
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.dx = 0.1                   #Reset speed
        ball.dy = 0.1
        ball.goto(0, 0)                 #Back to the center
        ball_restart_direction = random.randint(1,2)
        if (ball_restart_direction == 1):
            ball.dx *= -1               #Head towards the other side
        if (ball_restart_direction == 2):
            ball.dx *= -1
            ball.dy *= -1
        score_a += 1                    #Add score
        pen.clear()                     #Clear the pen so that words doesn't stack upon to each other
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.dx = -0.1
        ball.dy = 0.1
        ball.goto(0, 0)
        ball_restart_direction = random.randint(1,2)
        if (ball_restart_direction == 1):
            ball.dx *= -1
        if (ball_restart_direction == 2):
            ball.dx *= -1
            ball.dy *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    #Paddle and ball collisions
    if (ball.xcor() > 350 and ball.xcor() < 360) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() -60):
        ball.setx(340)
        ball.dx *= -1.05
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -350 and ball.xcor() > -360) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() -60):
        ball.setx(-340)
        ball.dx *= -1.05
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    #Paddle move restriction
    #A
    if (paddle_a.ycor() > 240):
        paddle_a.sety(240)
    elif(paddle_a.ycor() < -240):
        paddle_a.sety(-240)

    #B
    if (paddle_b.ycor() > 240):
        paddle_b.sety(240)
    elif(paddle_b.ycor() < -240):
        paddle_b.sety(-240)
