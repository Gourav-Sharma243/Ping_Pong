import turtle as tp
import winsound
wn=tp.Screen()
wn.title("Pong By Gourav")
wn.bgcolor("red")
wn.setup(width= 1200, height=700 )
wn.tracer(0)

#Score:
scoreA=0
scoreB=0

#Paddel A:
paddleA=tp.Turtle()
paddleA.speed(0)
paddleA.color('black')
paddleA.shape('square')
paddleA.shapesize(stretch_len=1,stretch_wid=5)
paddleA.penup()
paddleA.goto(-580,0)
paddleA.dx=1
paddleA.dy=1
#Paddle B
paddleB=tp.Turtle()
paddleB.speed(0)
paddleB.color('black')
paddleB.shape('square')
paddleB.shapesize(stretch_len=1,stretch_wid=5)
paddleB.penup()
paddleB.goto(580,0)
paddleB.dx=1
paddleB.dy=1

#Ball
ball=tp.Turtle()
ball.speed(0)
ball.color('black')
ball.shape('circle')
ball.penup()
ball.goto(0,0)
ball.dx=0.5
ball.dy=-0.5

#Pen
pen=tp.Turtle()
pen.speed(0)
pen.penup()
pen.color('white')
pen.hideturtle()
pen.goto(0,300)
pen.write("Player A:0   Player B:0",align="center",font=("Arial",24,"normal"))
#functions
def paddleA_up():
    y= paddleA.ycor()
    y+=20
    paddleA.sety(y)
def paddleA_down():
    y= paddleA.ycor()
    y-=20
    paddleA.sety(y)
def paddleB_up():
    y= paddleB.ycor()
    y+=20
    paddleB.sety(y)
def paddleB_down():
    y= paddleB.ycor()
    y-=20
    paddleB.sety(y)
#keywords
wn.listen()
wn.onkeypress(paddleA_up,"w")
wn.onkeypress(paddleB_up,"Up")
wn.onkeypress(paddleA_down,"s")
wn.onkeypress(paddleB_down,"Down")
#main loop
while True:
    wn.update()
#move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #border Checking
    if ball.ycor() > 350:
        ball.sety(350)
        ball.dy*=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.ycor() < -340:
        ball.sety(-340)
        ball.dy*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if ball.xcor() >650:
        ball.goto(0,0)
        ball.dx*=-1
        scoreA+=1
        pen.clear()
        pen.write("Player A :{}   Player B :{}".format(scoreA ,scoreB), align="center", font=("Arial", 24, "normal"))
    if ball.xcor() <-650:
        ball.goto(0,0)
        ball.dx*=-1
        scoreB += 1
        pen.clear()
        pen.write("Player A:{}   Player B:{}".format(scoreA ,scoreB), align="center", font=("Arial", 24, "normal"))

    #paddle and ball collision
    if(ball.xcor()> 570 and ball.xcor()< 580) and (ball.ycor() < paddleB.ycor()+40 and ball.ycor() > paddleB.ycor()-40):
        ball.setx(570)
        ball.dx*=-1
        winsound.PlaySound("bounce2.wav", winsound.SND_ASYNC)
    if (ball.xcor() <- 570 and ball.xcor() > -580) and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() - 40):
        ball.setx(-570)
        ball.dx *= -1
        winsound.PlaySound("bounce2.wav", winsound.SND_ASYNC)
    #border cheking paddle
    if paddleA.ycor() > 300:
        paddleA.sety(300)
    if paddleA.ycor() < -300:
        paddleA.sety(-300)
    if paddleB.ycor() <- 300:
        paddleB.sety(-300)
    if paddleB.ycor() > 300:
        paddleB.sety(300)

