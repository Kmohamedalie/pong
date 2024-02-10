# Simple Pong in Python 3 for Beginners
# By @kmohamedalie
# Part 1: Getting Started
# Part 2: Paddles and ball
# Part 3: Moving the paddles
# Part 4: Moving the ball
# Part 5: Colliding with the paddles
# Part 6: Scoreboard

#Gamers
def intro():
    print("Hello and welcome to the pong Game!")
intro()


name_1 = input("please enter player 1 name: ")
name_2 = input("please enter player 2 name: ")


import turtle, time
import winsound


screen = turtle.Screen()
screen.title("Pong by Baba & Alie")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Padddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

#Score
score_a = 0
score_b = 0

#center line
paddle_c = turtle.Turtle()
paddle_c.speed(0)
paddle_c.shape("square")
paddle_c.color("white")
paddle_c.shapesize(stretch_wid=26, stretch_len=0.001)
paddle_c.penup()
paddle_c.goto(0, 0)


#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f'{name_1}: {score_a}  {name_2}: {score_b}', align="center", font=("Courier", 24, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)



# Keyborad binding
screen.listen()
screen.onkeypress(paddle_a_up, "w")
screen.onkeypress(paddle_a_down, "s")
screen.onkeypress(paddle_b_up, "Up")
screen.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    screen.update()
    time.sleep(0.01)

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        #winsound.PlaySound("pong.mp3", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        #winsound.PlaySound("pong.mp3", winsound.SND_ASYNC)

    if ball.xcor() > 390: # Right side
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f'{name_1}: {score_a}  {name_2}: {score_b}', align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:# Left side
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f'{name_1}: {score_a}  {name_2}: {score_b}', align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

